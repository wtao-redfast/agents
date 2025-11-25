from engageManual import getRecurlyEngageDocs 
import os

def main():
    output = "output"
    if not os.path.exists(output):
        os.makedirs(output) 
    getRecurlyEngageDocs()


if __name__ == "__main__":
    main()
