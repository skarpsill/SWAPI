---
title: "Get Depth of Extrusion Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Depth_of_Extrusion_Example_VBNET.htm"
---

# Get Depth of Extrusion Example (VB.NET)

This example shows how to get the depth of an extrusion.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part containing a Boss-Extrude1 feature.
 ' 2. Open the Immediate window.
 '
 ' Postconditions: Examine the Immediate window.
 '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swDim As Dimension
         Dim vConfigNames As Object
         Dim vValue As Object

         swModel = swApp.ActiveDoc
         swDim = swModel.Parameter("D1@Boss-Extrude1")

         Debug.Assert(Not swDim Is Nothing)

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Full name = " & swDim.FullName)
         Debug.Print("  Name = " & swDim.Name)

         vConfigNames = swModel.GetConfigurationNames
         vValue = swDim.GetSystemValue3(swInConfigurationOpts_e.swThisConfiguration, (vConfigNames))

         Debug.Print("  System value = " & vValue(0) * 1000.0# & "" & " mm")

     End Sub

     Public swApp As SldWorks

 End  Class
```
