---
title: "Call Compiled HTML Help File Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Call_Compiled_HTML_Help_File_Example_CSharp.htm"
---

# Call Compiled HTML Help File Example (C#)

This example shows how to call a compiled HTML Help file.

'-------------------------------------

'

' Preconditions: Specified compiled HTML Help file exists.

'

' Postconditions: Compiled HTML Help file is displayed.

'

'-------------------------------------

public bool OnHelp()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}string
url = "E:/am/2005/C#/DisplayHelpFromPropMgr/apihelp.chm";

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}//Create
a basic form to be the basis for the Help file

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Windows.Forms.Form
helpForm = new System.Windows.Forms.Form();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}System.Windows.Forms.Help.ShowHelp(helpForm, url);

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
true;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}}
