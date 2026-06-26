---
title: "Get OLE Object Data Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_OLE_Object_Data_Example_CSharp.htm"
---

# Get OLE Object Data Example (C#)

This example shows how to get OLE object data from a model document.

```vb
  //----------------------------------------------------------
 // Preconditions:
 // 1. Open a model document.
 // 2. Click Insert > Object.
 // 3. Click Paintbrush Picture > OK.
 // 4. Click File > Close.
 // 5. Open the Immediate window.
 //
 // Postconditions: Inspect the Immediate window.
 //-----------------------------------------------------------
 using Microsoft.VisualBasic;
 using System;
 using System.Collections;
 using System.Collections.Generic;
 using System.Data;
 using System.Diagnostics;
 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System.Runtime.InteropServices;
 namespace GetOLEObjectData_CSharp.csproj
 {
     partial class SolidWorksMacro
     {

         ModelDoc2 swModel;
         ModelDocExtension swModelDocExt;
         SelectionMgr swSelMgr;
         SwOLEObject swOleObj;
         Boolean boolstatus;

         public void Main()
         {
             swModel = (ModelDoc2)swApp.ActiveDoc;
             swModelDocExt = swModel.Extension;
             swSelMgr = (SelectionMgr)swModel.SelectionManager;

             swOleObj = (SwOLEObject)swSelMgr.GetSelectedObject6(1, 0);

             Debug.Print("OLE Object");
             Debug.Print("  Class ID: " + swOleObj.Clsid);
             Debug.Print("  Is linked? " + swOleObj.IsLinked);
             Debug.Print("    Filename: " + swOleObj.FileName);
             Debug.Print("  Buffer size: " + swOleObj.BufferSize);
             Debug.Print("  Viewing aspect (1=Content, 2=Thumbnail, 4=Icon, 8=DocPrint): " + swOleObj.Aspect);

         }

         /// <summary>
         /// The SldWorks swApp variable is pre-assigned for you.
         /// </summary>

         public SldWorks swApp;

     }
 }
```
