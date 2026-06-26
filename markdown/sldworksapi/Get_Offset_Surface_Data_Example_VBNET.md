---
title: "Get Offset Surface Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Offset_Surface_Data_Example_VBNET.htm"
---

# Get Offset Surface Data Example (VB.NET)

This example shows how to get data for an offset surface.

```vb
 '------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly document that contains a component that
 '    has a surface offset feature.
 ' 2. Select the component's surface offset feature.
 ' 3. Open the Immediate window.
 '
 ' Postconditions: Inspect the Immediate window.
 '-----------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swSelData As SelectData
         Dim swOffset As SurfaceOffsetFeatureData
         Dim swFeat As Feature
         Dim swEnt As Entity
         Dim vFace As Object
         Dim i As  Long
         Dim bRet As Boolean
         Dim comp As Component2
         Dim swCompFace As Component2

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swOffset = swFeat.GetDefinition
         comp = swSelMgr.GetSelectedObjectsComponent3(1, -1)

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("CompFeature = " & comp.Name2)
         Debug.Print("  " & swFeat.Name)
         Debug.Print("    Distance       = " & swOffset.Distance * 1000.0# & " mm")
         Debug.Print("    Flip           = " & swOffset.Flip)
         Debug.Print("    FacesCount     = " & swOffset.GetEntitiesCount)

         bRet = swOffset.AccessSelections(swModel, comp)

         swModel.ClearSelection2(True)

         vFace = swOffset.Entities

         For i = 0 To UBound(vFace)
             swEnt = vFace(i)
             Debug.Print "    Entity selected = " & swEnt.Select4(True, Nothing)
             swCompFace = swEnt.GetComponent
             Debug.Print("    Component face = " & swCompFace.Name2)
         Next i

         swOffset.ReleaseSelectionAccess()

     End Sub

     Public swApp As SldWorks

 End  Class
```
