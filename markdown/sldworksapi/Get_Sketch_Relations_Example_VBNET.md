---
title: "Get Sketch Relations Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Relations_Example_VBNET.htm"
---

# Get Sketch Relations Example (VB.NET)

This example shows how to get all of the sketch relations in a sketch.

```vb
 '------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly document.
 ' 2. Select the sketch whose relations you want to see.
 '
 ' Postconditions: Inspect the Immediate window.
 '--------------------------------------------------------------------
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
         Dim swFeat As Feature
         Dim swSketch As Sketch
         Dim swSkRelMgr As SketchRelationManager
         Dim swSkRel As SketchRelation
         Dim dispDim As DisplayDimension
         Dim vSkRelArr As Object
         Dim vSkRel As Object
         Dim vEntTypeArr As Object
         Dim vEntType As swSketchRelationEntityTypes_e
         Dim vEntArr As Object
         Dim vDefEntArr As Object
         Dim swSkSeg As SketchSegment
         Dim swSkPt As SketchPoint
         Dim i As  Integer
         Dim j As  Integer
         Dim bRet As Boolean

         swModel = swApp.ActiveDoc
         swSelMgr = swModel.SelectionManager
         swSelData = swSelMgr.CreateSelectData
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature2
         swSkRelMgr = swSketch.RelationManager

         swModel.ClearSelection2(True)

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Feat = " & swFeat.Name)

         vSkRelArr = swSkRelMgr.GetRelations(swSketchRelationFilterType_e.swAll) : If IsNothing(vSkRelArr) Then Exit  Sub
         For Each vSkRel In vSkRelArr
             swSkRel = vSkRel

             Debug.Print("    Relation(" & i & ")")
             Debug.Print("      Type         = " & swSkRel.GetRelationType)

             dispDim = swSkRel.GetDisplayDimension
             If Not dispDim Is Nothing Then
                 Debug.Print("      Display dimension         = " & dispDim.GetNameForSelection)
             End If

             vEntTypeArr = swSkRel.GetEntitiesType
             vEntArr = swSkRel.GetEntities

             vDefEntArr = swSkRel.GetDefinitionEntities2
             If IsNothing(vDefEntArr) Then
             Else
                 Debug.Print("    Number of definition entities in this relation: " & UBound(vDefEntArr))
             End If

             If Not IsNothing(vEntTypeArr) And Not IsNothing(vEntArr) Then
                 If UBound(vEntTypeArr) = UBound(vEntArr) Then

                     j = 0

                     For Each vEntType In vEntTypeArr
                         Debug.Print("        EntType    = " & vEntType)

                         Select Case vEntType
                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Unknown
                                 Debug.Print("          Not known")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_SubSketch
                                 Debug.Print("SubSketch")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Point
                                 swSkPt = vEntArr(j) : Debug.Assert(Not swSkPt Is Nothing)

                                 Debug.Print("          SkPoint ID = [" & swSkPt.GetID(0)   ", " & swSkPt.GetID(1) & "]")

                                 bRet = swSkPt.Select4(True, swSelData) '

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Line, _
                                     swSketchRelationEntityTypes_e.swSketchRelationEntityType_Arc, _
                                     swSketchRelationEntityTypes_e.swSketchRelationEntityType_Ellipse, _
                                     swSketchRelationEntityTypes_e.swSketchRelationEntityType_Parabola, _
                                     swSketchRelationEntityTypes_e.swSketchRelationEntityType_Spline

                                 swSkSeg = vEntArr(j)

                                 Debug.Print("          SkSeg   ID = [" & swSkSeg.GetID(0)   ", " & swSkSeg.GetID(1) & "]")

                                 bRet = swSkSeg.Select4(True, swSelData)

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Hatch
                                 Debug.Print("Hatch")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Text
                                 Debug.Print("Text")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Plane
                                 Debug.Print("Plane")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Cylinder
                                 Debug.Print("Cylinder")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Sphere
                                 Debug.Print("Sphere")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Surface
                                 Debug.Print("Surface")

                             Case swSketchRelationEntityTypes_e.swSketchRelationEntityType_Dimension
                                 Debug.Print("Dimension")

                             Case Else
                                 Debug.Print("Something else")

                         End Select

                         j = j + 1

                     Next
                 End If
             End If

             i = i + 1

         Next

     End Sub

     Public swApp As SldWorks

 End  Class
```
