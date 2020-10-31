# Homework 3

## Submission instructions

* Due date and time: November 16 (Monday), 11:59 pm ET

* Carmen submission: 
Submit a .zip file named `name.number.zip` (e.g., `chao.209.zip`), which contains the following files
  - your completed python script `NaiveBayes.py` (for NaiveBayes - Question 1) [Bounus: Your report on impact of alpha with optimal alpha as `report.txt`]
  - your completed python script `hmm.py` (for Hidden Markov Model - Question 2)
 
* Collaboration: You may discuss the homework with your classmates. However, you need to write your own solutions and submit them separately. In your submission, you need to list with whom you have discussed the homework. Please list each classmate's name and name.number (e.g., Wei-Lun Chao, chao.209) as a row at the end of `NaiveBayes.py` and `hmm.py`. Please consult the syllabus for what is and is not acceptable collaboration.

## Implementation instructions

* Download or clone this repository.

* You will see two directories: `NaiveBayes` , `HMM`

* You will see a [`data-sentiment`](`NaiveBayes/data-sentiment/`) folder inside the  [`NaiveBayes/`](./NaiveBayes/) directory, which contains train data (`train/Positive.txt`, `train/Neutral.txt`, `train/Negative.txt`) and the test data (`test/Positive.txt`, `test/Neutral.txt`, `test/Negative.txt`) for  Question 1.

* You will see a [`data-pos`](`./HMM/data-pos/`) folder inside the [`HMM`](./HMM/) directory, which contains train data (`train.txt`,  `train_words.txt`) and the test data (`test.txt`,  `test_words.txt`) for  Question 2.

* Please use python3 and write your own solutions from scratch. 

* **Caution! python and NumPy's indices start from 0. That is, to get the first element in a vector, the index is 0 rather than 1.**

* If you use Windows, we recommend that you run the code in the Windows command line. You may use `py -3` instead of `python3` to run the code.

* Caution! Please do not import packages (like scikit learn or nltk) that are not listed in the provided code. Follow the instructions in each question strictly to code up your solutions. Do not change the output format. Do not modify the code unless we instruct you to do so. (You are free to play with the code but your submitted code should not contain those changes that we do not ask you to do.) A homework solution that does not match the provided setup, such as format, name, initializations, etc., will not be graded. It is your responsibility to make sure that your code runs with the provided commands and scripts.



# Introduction

In this homework, you are to implement NaiveBayes and HMM algorithm for tweet classifications

* In Question 1, you will play with the Twitter Senitment Analysis data, where each tweet is tagged as with either Positive, Negative, or Neutral sentiment.


* In Question 2, you will play with Twitter pos data data, where each word in the tweet is tagged corresponding part-of-speech tag.



# Question 1: NaiveBayes Classification (50 pts)

* You will implement NaiveBayes in this question. You are to amend your implementation into (`NaiveBayes.py`)[(./NaiveBayes/NaiveBayes.py)].

* There are many sub-functions in  [`NaiveBayes.py`](./NaiveBayes/NaiveBayes.py). You can ignore all of them but [`def train(self, training_set, training_labels, alpha=1)`](./NaiveBayes/NaiveBayes.py#L104) and [`def predict(self, test_doc)`](./NaiveBayes/NaiveBayes.py#L128). You need to extract the correspondig log probablities to complete this implementaion.

* Debugging Tips: print the variable [`sums`](./NaiveBayes/NaiveBayes.py#L129) and check if it is returning the expected values.
  

## Auto grader:

* You may run the following command to test your implementation<br/>
`python3 NaiveBayes.py`<br/>

* Note that, the auto grader is to check your implementation semantics. If you have syntax errors, you may get python error messages before you can see the auto_graders' results.

* Again, the auto_grader is just to simply check your implementation. It may not be used for your final grading.

## Bonus: (10 pts)

Improve the results on test set with different alpha value in [`def train(self, training_set, training_labels, alpha=1)`](./NaiveBayes/NaiveBayes.py#L104) and report the best alpha at `report.txt`.



# Question 2: HMM Tagging (50 pts)

 You will implement hidden markov model in this question. You are to amend your implementation into `hmm.py`.

* There are many classe and sub-functions in [`hmm.py`](./HMM/hmm.py). You can ignore all of them but [`def get_transition(self, prevNodes, curNodes)`](./HMM/hmm.py#L81). You need to extract the correspondig transition and emmision probablities to complete this implementaion.
  

## Auto grader:

* You may run the following command to test your implementation<br/>
`python3 hmm.py`<br/>

* Note that, the auto grader is to check your implementation semantics. If you have syntax errors, you may get python error messages before you can see the auto_graders' results.

* Again, the auto_grader is just to simply check your implementation. It may not be used for your final grading.

* Debugging Tips: print the probability values while updating [`best_prev`](./HMM/hmm.py#L101) variable and check it is assigned with the the highest probability ones.


# What to submit:

* Your completed python script `NaiveBayes.py`
* Your report on impact of alpha with optimal alpha as `report.txt` (Bonus)
* Your completed python script `hmm.py`

