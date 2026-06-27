---
title: "Visual C# Standalone and Add-in Applications"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/GettingStarted/Visual_C__Standalone_and_Add-in_Applications.htm"
---

# Visual C# Standalone and Add-in Applications

## Visual C# .NET Standalone and Add-in Applications

### Standalone Applications (.exe files)

To create an instance of the SOLIDWORKS software, your executable project
should contain lines of code similar to the following:

static void Main(string[] args)

{

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SldWorks.SldWorks
swApp;

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= new SldWorks.SldWorks();

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp.ExitApp();kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swApp
= null;kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

}

Additionally, you must have added[references to the SOLIDWORKS
type libraries](../Overview/Type_Libraries.htm).

### Add-in Applications (.dll files)

You can create a Visual C# .NET DLL add-in using theSOLIDWORKS C# Add-in
Templateincluded in the[SOLIDWORKS
API SDK](SolidWorks_API_Getting_Started_Overview.htm). See[SOLIDWORKS C# Add-in Template](../Overview/Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.htm)for details.
