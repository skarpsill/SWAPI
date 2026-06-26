---
title: "Insert Body-Delete/Keep Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Delete_Body_Feature_Example_VBNET.htm"
---

# Insert Body-Delete/Keep Feature Example (VB.NET)

This example shows how to insert a Body-Delete/Keep feature into a multibody part.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\multibody\multi_local.sldprt.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates Body-Delete/Keep 1 in the FeatureManager design tree.
 ' 2. Inspect the Immediate window.
 '
 ' NOTE: Because the model is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim myFeature As Feature
     Dim insDelBody As DeleteBodyFeatureData
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc
         ' Select body to delete
         boolstatus = Part.Extension.SelectByID2("Fillet5", "SOLIDBODY", 0.0592851881957586, 0.0409115950836281, -0.0197275812591329,  True, 0,  Nothing, 0)
         ' Create a Body-Delete/Keep feature
         myFeature = Part.FeatureManager.InsertDeleteBody2(False)

         insDelBody = myFeature.GetDefinition
         Debug.Print("Number of bodies in this Body-Delete/Keep feature: " & insDelBody.GetBodiesCount)
         Debug.Print("Keep bodies: " & insDelBody.KeepBodies)

     End Sub

     Public swApp As SldWorks

 End  Class
```
