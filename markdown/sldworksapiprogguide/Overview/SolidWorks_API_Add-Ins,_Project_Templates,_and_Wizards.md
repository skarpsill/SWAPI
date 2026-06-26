---
title: "SOLIDWORKS API Add-in Templates and Wizards"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SolidWorks_API_Add-Ins,_Project_Templates,_and_Wizards.htm"
---

# SOLIDWORKS API Add-in Templates and Wizards

The[SOLIDWORKS
API SDK](../GettingStarted/SolidWorks_API_Getting_Started_Overview.htm)contains:

- SOLIDWORKS
  C++/CLI COM Add-in Wizard(Visual C++/CLI - Microsoft Visual
  Studio 2005, 2008, 2010)
- **SOLIDWORKS C#
  and VB.NET Add-in Templates**

NOTE:While SOLIDWORKS recommends using ATL and their ATL-based
C++ wizards for creating C++ COM-based add-ins, if you are creating a
COM-style add-in and are using an MFC CCmdTarget-derived object to implement
ISwAddin, you must fully implement ITypeInfo as follows:

- In the declaration
  of your CCmdTarget-derived class, add:

- In your implementation,
  add:

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}*pIID
== IID_ISwAddin;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}return
TRUE;

}

- In your class constructor,
  add:

EnableTypeLib();

To learn more about add-ins and their menu items and toolbars:

- [Add-in Callbacks](Add-in_Callbacks.htm)
- [Add-in Icons](Add-in_Icons.htm)
- [Add-in Shortcut Menus](Add-in_Shortcut_Menus.htm)
- [Add-in Toolbars](Add-in_Toolbars.htm)

kadov_tag{{<implicit_p>}}
