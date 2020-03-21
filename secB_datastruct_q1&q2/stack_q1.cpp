#include<iostream>
#include<string>
#include<conio.h>
#include <stack>

using namespace std;

//Set Precedence of the operationaators
int precedence (char ope)
{
  if (ope == '+' || ope == '-')
    return 1;
  else if (ope == '*' || ope == '/')
    return 2;
  return 0;
}

//applying operationator to operationands
float eval (float a, float b, char op)
{
  switch (op)
    {
    case '+':
      return float (a + b);
      break;
    case '-':
      return float (a - b);
      break;
    case '*':
      return float (a * b);
      break;
    case '/':
      return float (a / b);
      break;
    }
  return 0;
}

float eval_stack (char x[], int size)
{
  /*stack-val for val
    stack-operation for operationators*/
  stack < float >val;
  stack < char >operation;
  //going thru the stack
  for (int i = 0; i < size; i++)
    {
      if (x[i] == ' ')
	continue;

      else if (x[i] == '(')
	operation.push (x[i]);

      
      else if (isdigit (x[i]))
	{ 
          //pushing digits into the stack
	  float a = 0;
	  while (i < size && isdigit (x[i]))
	    {
	      a = a * 10 + (x[i] - '0');
	      i++;
	    }
	  i--;
	  val.push (a);


	}
      //doing the operationation and then pushing it into the stack
      else if (x[i] == ')')
	{
          
	  while (!operation.empty () && operation.top () != '(')
	    {
	      float val1 = val.top ();
	      val.pop ();
	      float val2 = val.top ();
	      val.pop ();
	      char op = operation.top ();
	      operation.pop ();
	      val.push (eval (val2, val1, op));
	    }
	  if (!operation.empty ())
	    operation.pop ();
	}

      else
	{
	  if (operation.empty ())
	    operation.push (x[i]);
	  else
	    {

	      while (!operation.empty ()
		     && precedence (operation.top ()) >= precedence (x[i]))
		{
		  float val1 = val.top ();
		  val.pop ();
		  float val2 = val.top ();
		  val.pop ();
		  char op = operation.top ();
		  operation.pop ();
		  val.push (eval (val2, val1, op));
		}
	      operation.push (x[i]);

	    }

	}

    }

  while (!operation.empty ())
    {
      float val1 = val.top ();
      val.pop ();
      float val2 = val.top ();
      val.pop ();
      char op = operation.top ();
      operation.pop ();
      val.push (eval (val2, val1, op));
    }

  return val.top ();
}

int main ()
{
  int size = 0;
  //arithmetic expression is obtained as char array
  char a[100];
  cout << "Enter arithmetic expression:";
  cin.getline (a, 100);
  for (int n = 0; a[n] != NULL; ++n)
    size++;
  float answer = eval_stack (a, size);
  cout << "answer :" << answer;
  return 0;
}

