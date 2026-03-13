import webbrowser
import os

def main():
    print("Hello, Processor Design Task 2!")

    #path to html file
    file_path = os.path.abspath("index.html")

    #open in default browser
    webbrowser.open(f"file://{file_path}")


    while True:


        return


if __name__ == "__main__":
    main()