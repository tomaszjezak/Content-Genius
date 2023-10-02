import inspect
from termcolor import colored
from typing import Union, List
from steamship import check_environment, RuntimeEnvironments, Steamship, Tag
from steamship.invocable import post, PackageService

PROMPT_AUDIENCE = """
Your goal is to extract information from the user's input that matches the form described below. Extract an Output with <audience> for each Input.
  
<audience>: Extract the target audience of the following input. Only repond with the group of people that could be interested in this input

Input:
My business sells coaching on how to build an international social circle of motivated, driven young entrepreneurs.
Output:
Young male entrepreneurs

Input:
My business sells organic green juice and other high-quality health products in a brick-and-mortar store in LA
Output:
LA upper-middle-class health-conscious people; vegans

Input:
My busness sells 
Output:
TV viewers, people interested in media and pop culture

Input:
{story}
Output:
"""

PROMPT_TOPIC = """
Your goal is to extract information from the user's input that matches the form described below. Extract an Output with <topic> for each Input.
  
<topic>: Generate the the main topics of the following input. Only repond with two

Input:
Ruriko visits robot versions of her former bandmates, who are kept in a sex hotel. Through talking with them, she revisits the day all of them died, leaving her the sole survivor. 
Output:
Death and Technology

Input:
After a disaster wipes out most of the food supply, a young woman struggles to find hope and love in her new basecamp.
Output:
Survival and Romance

Input:
A TV critic begins to have trouble telling the difference between her own, real life, and the lives of the characters on television.
Output:
Television and Reality

Input:
{story}
Output:
"""
