---
title: "Using the SOLIDWORKS C# and VB.NET Add-in Templates to Create Add-ins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/SolidWorks_CSharp_and_VB.NET__Project_Templates.htm"
---

# Using the SOLIDWORKS C# and VB.NET Add-in Templates to Create Add-ins

This topic describes how to use theSOLIDWORKS
C# Add-in Templateor theSOLIDWORKS
VB.NET Add-in Templateto create an add-in using Microsoft Visual
Studio .NET 2005 and later.

After installing
the[SOLIDWORKS
API SDK](../GettingStarted/SolidWorks_API_Getting_Started_Overview.htm):

1. Open Microsoft Visual Studio .NET.
2. Click**File > New > Project**.
3. In the left panel of the New Project dialog, select:

  - Visual C#, scroll to the end of the middle panel, and select[SwCSharpAddin add-in template](Using_SolidWorks_C__Add-In_Wizard_to_Create_C__Add-In.htm).
  - Visual Basic, scroll to the end of the middle panel, and
    select[SwVBAddin add-in template](Using_SolidWorks_VB.NET_Add-In_Wizard_to_Create_VB.NET_Add-In.htm).
4. Modify the**Name**,**Location**,**Solution**, and**Solution name**fields.
5. Click**OK**.
6. Open Solution Explorer.
7. Double-click**SwAddin.***to open it.
8. Notice that SwAddin uses or imports SolidWorksTools. The SOLIDWORKS
  API SDK installs**SolidWorksTools.dll**in`install_dir`. The
  template adds this DLL to the reference list of your add-in project. The
  DLL must be redistributed with your add-in application. Currently this DLL contains the SOLIDWORKS bitmap handler class, BitmapHandler,
  which is based on the SOLIDWORKS CommandManager. Use either the Microsoft Visual Studio .NET Object Browser or Intellisense to see its members.
