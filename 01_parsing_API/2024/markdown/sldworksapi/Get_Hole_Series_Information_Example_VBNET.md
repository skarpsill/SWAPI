---
title: "Get Hole Series Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Hole_Series_Information_Example_VBNET.htm"
---

# Get Hole Series Information Example (VB.NET)

This example shows how to get information about a hole series.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open an assembly that contains a hole series feature.
 ' 2. Configure holes in the SOLIDWORKS Toolbox.
 '
 ' Postconditions: Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swDoc As ModelDoc2
     Dim SelMgr As SelectionMgr
     Dim boolstatus As Boolean
     Dim swFeat As Feature
     Dim swFeatData As HoleSeriesFeatureData2
     Dim swFace As Face2
     Dim swEnt As Entity

     Sub main()

         swDoc = swApp.ActiveDoc
         SelMgr = swDoc.SelectionManager
         swFeat = swDoc.FirstFeature

         Do While Not swFeat Is  Nothing
             Debug.Print(swFeat.GetTypeName & ", " & swFeat.Name)
             If swFeat.GetTypeName = "HoleSeries" Then
                 swFeatData = swFeat.GetDefinition
                 Debug.Print("  Standard:", swFeatData.Standard)

                 Dim i As  Integer

                 For i = 0 To swFeatData.GetComponentsCount - 1
                     Debug.Print("  Component " & i)
                     Debug.Print("    Type:", swFeatData.Type(i))
                     Debug.Print("    Size:", swFeatData.Size(i))
                 Next

                 Debug.Print("  FastenerMaterial:", swFeatData.Material)

                 ' Bolt and nut information causes an error
                 ' if SOLIDWORKS Toolbox is not configured
                 Debug.Print("  BoltHeadDiameter:", swFeatData.BoltHeadDiameter)
                 Debug.Print("  BoltDiameter:", swFeatData.BoltDiameter)
                 Debug.Print("  NutDiameter:", swFeatData.NutDiameter)
                 Debug.Print("  FastenerPreload:", swFeatData.Preload)
                 Debug.Print("  FastenerDefaultUnits:", swFeatData.FastenerDefaultUnits)
                 Debug.Print("  FastenerTopHoleType:", swFeatData.FastenerTopHoleType)
                 Debug.Print("  FastenerBottomHoleType:", swFeatData.FastenerBottomHoleType)
                 Debug.Print("  FastenerHoleCount:", swFeatData.FastenerHoleCount)

                 ' End face
                 swFeatData.AccessSelections(swDoc, Nothing)
                 swFace = swFeatData.EndFace
                 swEnt = swFace

                 If Not swEnt Is  Nothing  Then
                     boolstatus = swEnt.Select4(False, Nothing)
                     Debug.Print(" Face selection = " & boolstatus)
                 End If

                 ' Sketch points
                 Dim ncount As Integer
                 ncount = swFeatData.GetSketchPointsCount
                 Debug.Print(" Sketch Point Count = " & ncount)

                 Dim vPtArr As Object
                 vPtArr = swFeatData.GetSketchPoints

                 Dim swSketchPoint As SketchPoint

                 For i = 0 To i = ncount - 1
                     swSketchPoint = vPtArr(i)
                     swSketchPoint.Select4(False, Nothing)
                 Next

                 ' Components
                 ncount = swFeatData.GetComponentsCount
                 Debug.Print("  ComponentsCount Count = " & ncount)
                 vPtArr = swFeatData.GetComponents
                 Dim swComp As Component

                 For i = 0 To i = ncount - 1
                     swComp = vPtArr(i)
                     If Not swComp Is  Nothing  Then
                         Debug.Print("  " & swComp.Name2 & " --> " & swComp.GetPathName)
                     Else
                         Debug.Print("  Could not get component.")
                     End If
                 Next

                 swFeatData.ReleaseSelectionAccess()

             End If

             swFeat = swFeat.GetNextFeature

         Loop

     End Sub

     Public swApp As SldWorks

 End  Class
```
