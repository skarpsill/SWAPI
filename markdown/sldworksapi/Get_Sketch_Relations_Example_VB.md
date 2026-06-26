---
title: "Get Sketch Relations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Relations_Example_VB.htm"
---

# Get Sketch Relations Example (VBA)

This example shows how to get all of the sketch relations in a sketch.

```vb
 '------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a part or assembly document.
 ' 2. Select the sketch whose relations you want to see.
 '
 ' Postconditions: Inspect the Immediate window.
 '--------------------------------------------------------------------
Option Explicit

Sub main()
    Dim swApp                           As SldWorks.SldWorks
     Dim swModel                         As SldWorks.ModelDoc2
     Dim swSelMgr                        As SldWorks.SelectionMgr
     Dim swSelData                       As SldWorks.SelectData
     Dim swFeat                          As SldWorks.Feature
     Dim swSketch                        As SldWorks.Sketch
     Dim swSkRelMgr                      As SldWorks.SketchRelationManager
     Dim swSkRel                         As SldWorks.SketchRelation
     Dim dispDim                         As SldWorks.DisplayDimension
     Dim vSkRelArr                       As Variant
     Dim vSkRel                          As Variant
     Dim vEntTypeArr                     As Variant
     Dim vEntType                        As Variant
     Dim vEntArr                         As Variant
     Dim vEnt                            As Variant
     Dim vDefEntArr                      As Variant
     Dim swSkSeg                         As SldWorks.SketchSegment
     Dim swSkPt                          As SldWorks.SketchPoint
     Dim i                               As Long
     Dim j                               As Long
     Dim bRet                            As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSketch = swFeat.GetSpecificFeature2
     Set swSkRelMgr = swSketch.RelationManager
    swModel.ClearSelection2 True
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Feat = " & swFeat.Name
    vSkRelArr = swSkRelMgr.GetRelations(swAll): If IsEmpty(vSkRelArr) Then Exit Sub
     For Each vSkRel In vSkRelArr
         Set swSkRel = vSkRel
        Debug.Print "    Relation(" & i & ")"
         Debug.Print "      Type         = " & swSkRel.GetRelationType

         Set dispDim = swSkRel.GetDisplayDimension
        If Not dispDim Is Nothing Then
             Debug.Print "      Display dimension = " & dispDim.GetNameForSelection
         End If
        vEntTypeArr = swSkRel.GetEntitiesType
         vEntArr = swSkRel.GetEntities

        vDefEntArr = swSkRel.GetDefinitionEntities2
         If IsEmpty(vDefEntArr) Then
         Else
             Debug.Print "    Number of definition entities in this relation: " & UBound(vDefEntArr)
         End If

        If Not IsEmpty(vEntTypeArr) And Not IsEmpty(vEntArr) Then
           If UBound(vEntTypeArr) = UBound(vEntArr) Then
            j = 0

            For Each vEntType In vEntTypeArr
                 Debug.Print "        EntType    = " & vEntType

                Select Case vEntType
                     Case swSketchRelationEntityType_Unknown
                         Debug.Print "          Not known"

                    Case swSketchRelationEntityType_SubSketch
                         Debug.Print "SubSketch"

                    Case swSketchRelationEntityType_Point
                         Set swSkPt = vEntArr(j): Debug.Assert Not swSkPt Is Nothing

                        Debug.Print "          SkPoint ID = [" & swSkPt.GetID(0) & ", " & swSkPt.GetID(1) & "]"

                        bRet = swSkPt.Select4(True, swSelData) '

                    Case swSketchRelationEntityType_Line, _
                             swSketchRelationEntityType_Arc, _
                             swSketchRelationEntityType_Ellipse, _
                             swSketchRelationEntityType_Parabola, _
                             swSketchRelationEntityType_Spline

                        Set swSkSeg = vEntArr(j)

                        Debug.Print "          SkSeg   ID = [" & swSkSeg.GetID(0) & ", " & swSkSeg.GetID(1) & "]"

                        bRet = swSkSeg.Select4(True, swSelData)

                    Case swSketchRelationEntityType_Hatch
                         Debug.Print "Hatch"

                    Case swSketchRelationEntityType_Text
                         Debug.Print "Text"

                    Case swSketchRelationEntityType_Plane
                         Debug.Print "Plane"

                    Case swSketchRelationEntityType_Cylinder
                         Debug.Print "Cylinder"

                    Case swSketchRelationEntityType_Sphere
                         Debug.Print "Sphere"

                    Case swSketchRelationEntityType_Surface
                         Debug.Print "Surface"

                    Case swSketchRelationEntityType_Dimension
                         Debug.Print "Dimension"

                    Case Else
                         Debug.Print "Something else"

                End Select

                j = j + 1

            Next
           End If
         End If

        i = i + 1
    Next
End Sub
```
