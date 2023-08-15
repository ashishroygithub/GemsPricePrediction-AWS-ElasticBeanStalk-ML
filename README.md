# Gemstone Price Prediction - Ashish Roy

##### PrereqiPrerequisites - GitHub, New Env, Setup file

**GitHub**

#### Step by step Implemenatation. - GitHub

* `Step 1` : Get your GitHub in sync with Visual Code.

* `Step 2` : Set up a virtual Environment: `conda create -p venv python==3.8 -y` (This will create a conda environment and install necessary libraries)

* `Step 3` : Activate the virtual environment: `conda activate venv/`

* `Step 4` : `Next process is to clone the entire repository so that we are able to commit our code.`
    * echo "#GemsPricePrediction-AWS-ElasticBeanStalk-Codepipeline" >> README.md
    * git init
    * git add README.md
    * git commit -m "first commit"
    * git branch -M main
    * git remote add origin https://github.com/ashishroygithub/GemsPricePrediction-AWS-ElasticBeanStalk-Codepipeline.git
    * git push -u origin main

* `Step 5` : `For Existing Repository:`
    * git remote add origin https://github.com/ashishroygithub/GemsPricePrediction-AWS-ElasticBeanStalk-Codepipeline.git
    * git branch -M main
    * git push -u origin main

* `Step 6` : `You can use the below commands to add the new files which have been created on vs-code step by step`
    * git add . (This adds all the new file into the repository)
    * git status (you can use this to check the status of the command)
    * git commit -m "Comments" (you can use this to add the comments during push)
    * git push -u origin main (This is where you push the code to the github repository)
    * git pull (If you have made any changes into the github repository, this will help to pull the same)

#### Step by step Implemenatation. - GITBash

## If you have not installed GIT then go-ahead and install GITBash (This will help in cloning the repository which is present on VsCode with github)

*** IF you are initializing GIT for the first time and then you get an error of authorization : ***

* `Step 1` : Use your terminal and write these commands below :

    * git config --global user.email "ashishgithubprojects@gmail.com"
    * git config --global user.name "ashishroygithub"
    * git config --local user.name "ashishroygithub"
    * git status == This command will help in adding the environment.
    * after git remote add: you can use this function to check  “ git remote -v “
    * create a .gitignore file on the GitHub webpage (reason for creating it is that we can ignore certain files that doesn’t require to be commited) some of the common things.
    * “git pull” function is basically use to download all the files.

* `Step 2` : If you are getting permission denied response then you can use the below to solve the issue.

    * git remote set-url origin https://user_name@github.com/username/repository_name.git

##### MAPPING HAS BEEN COMPLETED.

##### Things to remember : `"requirements.txt"`

### Edit : when you are facing an issue of this : `Traceback (most recent call last): File "src/components/data_ingestion.py", line 3, in <module> from src.exception import CustomException ModuleNotFoundError: No module named 'src'` - * *Solution* * : "pip install -e ." inside the terminal.

* when you want to trigger "setup.py" inside the requirements.txt file then you mention "-e .", if not then you just # "-e ." when you are directly trying to run the setup.py file (This second one can be # when you are trying to deploy it on the cloud.)

* you can use `pip install -r requirements.txt` to run all the packages, but if you are using it on the deployment stage then make sure you hastag this #-e .


**Files Created:**

01. GemStonePricePrediction/`setup.py`
02. GemStonePricePrediction/`requirements.txt`
03. GemStonePricePrediction/`.gitignore`
04. GemStonePricePrediction/`README.md`
05. GemStonePricePrediction/src/`__init__.py`
06. GemStonePricePrediction/src/`exception.py`
07. GemStonePricePrediction/src/`logger.py`
08. GemStonePricePrediction/src/`utils.py`
09. GemStonePricePrediction/src/components/`__inti__.py`
10. GemStonePricePrediction/src/components/`data_ingestion.py`
11. GemStonePricePrediction/src/components/`data_transformation.py`
12. GemStonePricePrediction/src/components/`model_trainer.py`
13. GemStonePricePrediction/src/pipeline/`__init__.py`
14. GemStonePricePrediction/src/pipeline/`predict_pipeline.py`
15. GemStonePricePrediction/src/pipeline/`train_pipeline.py`


### Introduction About the Data :

Please this project is of a student. Just wanted to appreciate for knowledge sharing 

**The dataset** The goal is to predict `price` of given diamond (Regression Analysis).

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

Dataset Source Link :
[https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv](https://www.kaggle.com/competitions/playground-series-s3e8/data?select=train.csv)

### It is observed that the categorical variables 'cut', 'color' and 'clarity' are ordinal in nature

### Check this link for details : [American Gem Society](https://www.americangemsociety.org/ags-diamond-grading-system/)

### ALWAYS Run "pip install -e ." this will trigger the setup file. 


##### DEPLOYMENT - AWS - ELASTIC BEAN STALK + CODEPIPELINE

* `Step 1` : Build Environment on Elastic Bean stock > create application > create Environment > choose Python > 3.8 > create Environment

* `Step 2` : Build A code Pipeline : Give Pipeline name > choose source provider (Github) > Connect your github > choose your repo and branch > skip build stage > Deploy provider (choose Elastic bean stock and fill in the info) > Create Pipeline.


#### IMPORTANT : .ebextensions is very important folder as it contains python.config file and it helps to push it to the EBS platform (and change app.py to application.py)


