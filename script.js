//Funtion for generating the table given the number of variables n from the user
function generateTable() {

    let n = parseInt(document.getElementById("numVars").value);
    let rows = Math.pow(2, n);

    let table = "<table border='1'><tr>";

    for (let i = 0; i < n; i++) {
        table += "<th>" + String.fromCharCode(65 + i) + "</th>";
    }

    table += "<th>Output</th></tr>";

    for (let i = 0; i < rows; i++) {

        table += "<tr>";

        let binary = i.toString(2).padStart(n, '0');

        for (let bit of binary) {
            table += "<td>" + bit + "</td>";
        }

        table += `<td><input type="text" id="out${i}" size="1"></td>`;

        table += "</tr>";
    }

    table += "</table>";

    document.getElementById("tableContainer").innerHTML = table;

}

//Function to generate the expression and validate the truth table inputs
function generateExpression() {

    let n = parseInt(document.getElementById("numVars").value);
    let rows = Math.pow(2, n);

    let form = document.querySelector('input[name="form"]:checked').value;

    let expression = [];
    let jsonOutput = {
        variables: n,
        form: form,
        rows: []
    };

    for (let i = 0; i < rows; i++) {

        let inputBox = document.getElementById("out" + i);
        let value = inputBox.value.trim();

        inputBox.classList.remove("invalid");

        if (value !== "0" && value !== "1") {
            inputBox.classList.add("invalid");
            continue;
        }

        let binary = i.toString(2).padStart(n, '0');

        jsonOutput.rows.push({
            inputs: binary,
            output: value
        });

        // SOP → rows with 1
        if (form === "SOP" && value === "1") {

            let term = "";

            for (let j = 0; j < n; j++) {

                let variable = String.fromCharCode(65 + j);

                if (binary[j] === "1")
                    term += variable;
                else
                    term += variable + "'";
            }

            expression.push(term);
        }

        // POS → rows with 0
        if (form === "POS" && value === "0") {

            let termParts = [];

            for (let j = 0; j < n; j++) {

                let variable = String.fromCharCode(65 + j);

                if (binary[j] === "1")
                    termParts.push(variable + "'");
                else
                    termParts.push(variable);
            }

            expression.push("(" + termParts.join(" + ") + ")");
        }

    }

    let exprString;

    if (form === "SOP")
        exprString = expression.join(" + ");
    else
        exprString = expression.join("");

    document.getElementById("result").innerText = exprString;

    jsonOutput.expression = exprString;

    console.log(JSON.stringify(jsonOutput, null, 2));

}