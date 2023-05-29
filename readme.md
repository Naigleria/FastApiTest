# 2 ways to execute fastapi

  1- uvicorn main:app
  2- Add the following lines of code
    if __name__=="__main__":
      uvicorn.run("main:app", port=8000)
    and the run  main.py