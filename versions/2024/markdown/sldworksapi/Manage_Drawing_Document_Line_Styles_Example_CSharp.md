---
title: "Manage Drawing Document Line Styles Example (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Manage_Drawing_Document_Line_Styles_Example_CSharp.htm"
---

# Manage Drawing Document Line Styles Example (C#)

This example shows how to manage the line styles of a drawing document.

```vb
  //---------------------------------------------------------------
 // Preconditions:
 // 1. Verify that the specified drawing document template exists.
 // 2. Ensure that c:\temp exists.
 // 3. Open an Immediate Window.
 //
 // Postconditions:
 // 1. Opens a new drawing.
 // 2. Adds line styles.
 // 3. Saves lines styles.
 // 4. Deletes a line style.
 // 5. Loads saved line styles, replacing existing line styles.
 // 6. Inspect the Immediate window.
 //
 // NOTE: Line styles are saved to c:\temp\styles.sldlin.
 //---------------------------------------------------------------

 using SolidWorks.Interop.sldworks;
 using SolidWorks.Interop.swconst;
 using System;
 using System.Diagnostics;
 namespace DrawingLineStyles_CSharp.csproj
 {
     partial class SolidWorksMacro
     {
         DrawingDoc Part;
         bool boolstatus;
         int longstatus;

         public void Main()
         {
             string def = null;
             string name = null;

             Part = (DrawingDoc)swApp.NewDocument("C:\\ProgramData\\SOLIDWORKS\\SOLIDWORKS 2016\\templates\\drawing.drwdot", 2, 0.2794, 0.4318);
             swApp.ActivateDoc2("Draw1 - Sheet1",  false, ref longstatus);

             printData("Line Style Data at Start",  "");

             def = "B,1.2,-0.2,2,-0.1,2";
             name = "NewOne";
             boolstatus = Part.AddLineStyle(name, def);
             printData("Line Style Data After Add",  "");

             object names = null;
             string[] styleNames = new string[3];

             styleNames[0] = "NewOne";
             styleNames[1] = "CHAIN";
             styleNames[2] = "PHANTOM";

             names = styleNames;

             // Save line styles
             boolstatus = Part.SaveLineStyles("c:\\temp\\styles", names, true);
             printData("Line Style Data saved to file ",  "c:\\temp\\styles");

             // Delete a line style
             boolstatus = Part.DeleteLineStyle("NewOne", "STITCH");
             printData("Line Style Data After Delete",  "");

             // Load saved line styles, replacing existing line styles
             boolstatus = Part.LoadLineStyles("c:\\temp\\styles", names, true);
             printData("Line Style Data Imported from file",  "");
         }

         public void printData(string title, string file)
         {
             object names = null;
             object types = null;
             string[] namesArr = null;
             string[] typesArr = null;
             int i = 0;
             bool stat = false;

             Debug.Print("-------------------------");
             Debug.Print(title);
             Debug.Print("-------------------------");

             if (string.IsNullOrEmpty(file))
             {
                 stat = Part.GetLineStyles(out names, out types);
             }
             else
             {
                 stat = swApp.GetLineStyles(file,  out names,  out types);
             }
             namesArr = (string[])names;
             typesArr = (string[])types;
             if (stat)
             {
                 for (i = 0; i <= typesArr.GetUpperBound(0); i++)
                 {
                     Debug.Print(i + " " + namesArr[i] + " " + typesArr[i]);
                 }
             }
             else
             {
                 Debug.Print("Error in printData");
             }
         }
         public SldWorks swApp;
     }
 }
```
