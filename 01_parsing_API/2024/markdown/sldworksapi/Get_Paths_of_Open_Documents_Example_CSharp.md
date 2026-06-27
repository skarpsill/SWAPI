---
title: "Get Paths of Open Documents (C#)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Paths_of_Open_Documents_Example_CSharp.htm"
---

# Get Paths of Open Documents (C#)

This example shows how to get an array of the open documents, and their
paths and filenames, in the current SOLIDWORKS session.

```vb
 //---------------------------------------------------------------------------
// Preconditions: At least one model document is
// kadov_tag{{<spaces>}}               kadov_tag{{</spaces>}}open in SOLIDWORKS.
//
// Postconditions: None.
 //---------------------------------------------------------------------------
using SolidWorks.Interop.sldworks;
using SolidWorks.Interop.swconst;
using System;
using System.Diagnostics;
using System.Runtime.InteropServices;
namespace GetOpenDocPaths_CSharp.csproj
{
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}public partial class SolidWorksMacro
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}ModelDoc2 swModel;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}object[] models;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int count;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}int index;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}string pathName;
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public void Main()
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}count = swApp.GetDocumentCount();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print("Number of open documents in this SOLIDWORKS session: " + count);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}models = (object[])swApp.GetDocuments();
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}for (index = 0; index < count; index++)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}{
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}swModel = models[index] as ModelDoc2;
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}pathName = swModel.GetPathName();
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print("Path and name of open document: " + pathName);
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// <summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// kadov_tag{{<spaces>}} kadov_tag{{</spaces>}}The SldWorks swApp variable is pre-assigned for you.
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}/// </summary>
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}public SldWorks swApp;
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}}
}
```
