---
title: "Create Sketch Path Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Path_Example_VB.htm"
---

# Create Sketch Path Example (VBA)

This example shows how to create a sketch path.

```vb
 '---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified document template exists.
 ' 2. Open an Immediate window.
 '
 ' Postconditions:
 ' 1. Creates a new model document with Sketch1.
 ' 2. Selects the Sketch1 segments.
 ' 3. Creates a sketch path.
 ' 4. Creates a sketch circle.
 ' 5. Adds a tangent relation between the sketch path and sketch circle.
 ' 6. Inspect the Immediate window.
 '---------------------------------------------------------------------------
 Dim swApp                           As SldWorks.SldWorks
 Dim swModel                         As SldWorks.ModelDoc2
 Dim swSelMgr                        As SldWorks.SelectionMgr
 Dim swFeat                          As SldWorks.Feature
 Dim swSketch                        As SldWorks.Sketch
 Dim i                               As Long
 Dim bRet                            As Boolean
 Dim vSketchPath                     As Variant
 Dim swSketchPath                    As SldWorks.SketchPath
 Dim nLength                         As Double
 Dim vConstraint                     As Variant
 Dim swSkRel                         As SldWorks.SketchRelation
 Dim vRelation                       As Variant
 Dim vSkRel                          As Variant
 Dim vSketchSeg                      As Variant
 Dim swSketchSeg                     As SldWorks.SketchSegment
 Dim swSketchMgr                     As SldWorks.SketchManager
 Dim boolstatus As Boolean

 Option Explicit
 Sub main()
    Set swApp = Application.SldWorks
     Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
     Set swModel = swApp.ActiveDoc

    swModel.SketchManager.InsertSketch True
     boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -4.16217612836357E-02, 2.70960165695038E-02, 3.55460240358513E-03, False, 0, Nothing, 0)

     Dim skSegment As Object
     Set skSegment = swModel.SketchManager.CreateLine(-0.055655, 0.037535, 0#, 0.011848, 0.039924, 0#)
     Set skSegment = swModel.SketchManager.CreateLine(0.011848, 0.039924, 0#, 0.018817, 0.009658, 0#)
     Set skSegment = swModel.SketchManager.CreateLine(0.018817, 0.009658, 0#, 0.05227, 0.008264, 0#)
     Set skSegment = swModel.SketchManager.CreateLine(0.05227, 0.008264, 0#, 0.065809, 0.036414, 0#)

     swModel.SketchManager.InsertSketch True

    Set swSelMgr = swModel.SelectionManager
     Set swSketchMgr = swModel.SketchManager
   ' Select the sketch
     bRet = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
     Set swSketch = swFeat.GetSpecificFeature2
    ' Put the sketch in edit mode
     swModel.EditSketch

    ' Get the sketch segments
     vSketchSeg = swSketch.GetSketchSegments

    For i = 0 To UBound(vSketchSeg)
         Set swSketchSeg = vSketchSeg(i)
         swSketchSeg.Select4 True, Nothing
     Next

    ' Create a chain using the selected sketch segments
     bRet = swSketchMgr.MakeSketchChain
     swModel.ClearSelection2(True)

    ' Get the sketch path
     vSketchPath = swSketch.GetSketchPaths
    ' Create a circle
     swModel.CreateCircle -0.07515069296375, 0.04810565031983, 0, -0.06525335820896, 0.04189104477612, 0

    ' Add a tangent relation between sketch path and sketch circle
     boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -5.44261072733269E-02, 4.71088420855688E-02, -3.28513702299429E-03, False, 0, Nothing, 0)
     boolstatus = swModel.Extension.SelectByID2("Line1", "SKETCHSEGMENT", -4.22450565500339E-02, 3.67651345154678E-02, -2.68554920844266E-03, True, 0, Nothing, 0)
     swModel.SketchAddConstraints ("sgTANGENT")

    ' Print the number of constraints, number of relations,
     ' path length, number of sketch segments, whether the path was selected,
     ' type of constraints, and type of relations
     For i = 0 To UBound(vSketchPath)
        Set swSketchPath = vSketchPath(i)
         Debug.Print " Number of constraints: " & swSketchPath.GetConstraintsCount
         Debug.Print " Number of relations: " & swSketchPath.GetRelationsCount
         Debug.Print " Path length: " & swSketchPath.GetLength
         Debug.Print " Number of segments: " & swSketchPath.GetSketchSegmentCount
         Debug.Print " Selection result: " & swSketchPath.Select(False, Nothing)
        vConstraint = swSketchPath.GetConstraints
        Dim j As Integer
         j = 0
        If (Not IsEmpty(vConstraint)) Then
             For j = 0 To UBound(vConstraint)
                 Debug.Print "  SketchSegConstraint[" & i & "]: " & vConstraint(j)
             Next j
         End If
        vRelation = swSketchPath.GetRelations
        Dim k As Integer
         k = 0
        For Each vSkRel In vRelation
              Set swSkRel = vSkRel
              Debug.Print "    Relation(" & k & ")"
              Debug.Print "      Type: " & swSkRel.GetRelationType
              k = k + 1
         Next
        ' Get the sketch segments in the sketch path and
         ' their lengths
         vSketchSeg = swSketchPath.GetSketchSegments
        Dim l As Integer
         For l = 0 To UBound(vSketchSeg)
            Set swSketchSeg = vSketchSeg(l)
            ' Ignore construction lines
             If swSketchSeg.ConstructionGeometry = False Then
                 ' Ignore text
                 If swSketchTEXT <> swSketchSeg.GetType Then
                     nLength = nLength + swSketchSeg.GetLength
                 End If
             End If
        Next l
        Debug.Print " Total path length calculated by segment: " & nLength
    Next
    swModel.SketchManager.InsertSketch True

 End Sub
```
