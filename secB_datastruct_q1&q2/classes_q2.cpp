/*All member variables are made private and member
 functions are made public.
 Topics are named as '1','2' and so on
 The string and the topic are the only inputs obtained from the user.
 The program uses a single publisher and 4 subscriber and 7 topics(static)
 Dynamic allocation could be done by getting user's input
*/
  




#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<dos.h>

class Publisher
{

  char str[50];
  //t refers to the topic on which the message will be published
  char t;
public:

    Publisher ()
  {
    std::cout << "Enter the string to be published : ";                                       
    std::cin >> str;
    std::cout << "Enter the topic to which message is to published : ";
    std::cin >> t;

  }

  char msg_topic ()
  {
    return t;
  }
  //publishes the string( pub command in ROS)
  char *publish ()
  {
    return str;
    
  }

};

class Subscriber
{
  char str[50];
  char topic;     
  //topic subscribed by the subscriber

public:

  //subscriber subscribes to a particular topic
  void topicf (char t)     
  {
    topic = t;          
  }
  char view_topic ()
  {
    return topic;         
  }
  // saving the string message
  void subscribed_msg (char *a)    
  {
    for (int i = 0; i < 50; i++)
      {
	str[i] = *a;
	a++;
      }
  }
  char *get_sub_data ()
  {
    return str;
  }
};

class Master
{

  Publisher P;        //class objects
  Subscriber S[4];
  char a, b, c, d, e, f, g; //topic variables
  char *Ma;
  char *Mb;
  char *Mc;
  char *Md;           //pointers pointing to the string message.Each for one topic
  char *Me;
  char *Mf;
  char *Mg;

public:

    Master ()
  {
    a = '1';
    b = '2';
    c = '3';
    d = '4';      //7 topics
    e = '5';
    f = '6';
    g = '7';
  }
  
  
  void assign_subscription ()
  {
    srand (time (NULL));
    int ch[4];
    std::cout << "Assinging topics to Subscribers(Randomly)....";
    delay (1000);
    for (int i = 0; i < 4; i++)
      {
	ch[i] = (rand () % 7);   //Random allocation of topics to the subscriber.To minimize user's  intervention
	switch (ch[i])
	  {
	  //if random no is 0,topic a is assigned and so on
	  case 0:
	    S[i].topicf (a);
	    break;
	  case 1:
	    S[i].topicf (b);
	    break;
	  case 2:
	    S[i].topicf (c);           
	    break;
	  case 3:
	    S[i].topicf (d);
	    break;
	  case 4:
	    S[i].topicf (e);
	    break;
	  case 5:
	    S[i].topicf (f);
	    break;
	  case 6:
	    S[i].topicf (g);
	    break;
	  }
      }

  }

  void handle_msg ()
  {
    char ch;
    ch = P.msg_topic ();
    std::cout <<
      "Publishing message to Master and Saving it to Subscriber,,,,";
    delay (1000);
    /*By checking if the subscriber has subscribed to the given input topic, messge gets 
      transmitted from publisher to subscriber by storing it in Master strings*/
    switch (ch)
      {
      case '1':
	Ma = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '1')
	      S[i].subscribed_msg (Ma);
	  }
	break;
      case '2':
	Mb = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '2')        
	      S[i].subscribed_msg (Mb);           
	  }
	break;
      case '3':
	Mc = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '3')
	      S[i].subscribed_msg (Mc);
	  }
	break;
      case '4':
	Md = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '4')
	      S[i].subscribed_msg (Md);
	  }
	break;
      case '5':
	Me = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '5')
	      S[i].subscribed_msg (Me);
	  }
	break;
      case '6':
	Mf = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '6')
	      S[i].subscribed_msg (Mf);
	  }
	break;
      case '7':
	Mg = P.publish ();
	for (int i = 0; i < 4; i++)
	  {
	    if (S[i].view_topic () == '7')
	      S[i].subscribed_msg (Mg);
	  }
	break;
      }

  }
  //member functions to display pub and sub data
  char getA ()             
  {
    return P.msg_topic ();
  }
  char *getB ()
  {
    return P.publish ();    
  }
  char getC (int a)
  {
    return S[a].view_topic ();
  }
  char *getD (int a)
  {
    return S[a].get_sub_data ();
  }
};

int
main ()
{
  int flag = 0;
  Master M;              //declaring the Master object(similar to calling the roscore)    
  M.assign_subscription (); //master assigns the topics
  M.handle_msg ();          //master gets data from publisher and sends to subscriber
  std::cout << "Loading info(abt the data transfer via Master)....";
  delay (1000);
  std::cout << "Published message :" << M.getB () << "\n";
  std::cout << "Published topic : " << M.getA () << "\n";
  for (int i = 0; i < 4; i++)
    {
      if (M.getA () == M.getC (i))
	{
	  std::cout << "Topic subscribed by Subscriber " << i +
	    1 << ":" << M.getC (i) << '\n';
	  std::cout << "Message sent to the Subscriber " << i +          
	    1 << ":" << M.getD (i);
	}
      else
	{
	  flag += 1;
	  continue;
	}

    }
  if (flag == 4)
    {
      std::cout << "No subscriber has subscribed to this Topic";
    }
  return 0;
}
