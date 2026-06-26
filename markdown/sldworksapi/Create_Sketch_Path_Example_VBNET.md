---
title: "Create Sketch Path Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Sketch_Path_Example_VBNET.htm"
---

# Create Sketch Path Example (VB.NET)

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
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim swSelMgr As SelectionMgr
     Dim swFeat As Feature
     Dim swSketch As Sketch
     Dim i As Integer
     Dim bRet As Boolean
     Dim vSketchPath As Object
     Dim swSketchPath As SketchPath
     Dim nLength As Double
     Dim vConstraint As Object
     Dim swSkRel As SketchRelation
     Dim vRelation As Object
     Dim vSkRel As Object
     Dim vSketchSeg As Object
     Dim swSketchSeg As SketchSegment
     Dim swSketchMgr As SketchManager
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
         swModel = swApp.ActiveDoc

         swModel.SketchManager.InsertSketch(True)
         boolstatus = swModel.Extension.SelectByID2("Front Plane", "PLANE", -0.0416217612836357, 0.0270960165695038, 0.00355460240358513, False, 0, Nothing, 0)

         Dim skSegment As Object
         skSegment = swModel.SketchManager.CreateLine(-0.055655, 0.037535, 0.0#, 0.011848, 0.039924, 0.0#)
         skSegment = swModel.SketchManager.CreateLine(0.011848, 0.039924, 0.0#, 0.018817, 0.009658, 0.0#)
         skSegment = swModel.SketchManager.CreateLine(0.018817, 0.009658, 0.0#, 0.05227, 0.008264, 0.0#)
         skSegment = swModel.SketchManager.CreateLine(0.05227, 0.008264, 0.0#, 0.065809, 0.036414, 0.0#)

         swModel.SketchManager.InsertSketch(True)

         swSelMgr = swModel.SelectionManager
         swSketchMgr = swModel.SketchManager

         ' Select the sketch
         bRet = swModel.Extension.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)

         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature2

         ' Put the sketch in edit mode
         swModel.EditSketch()

         ' Get the sketch segments
         vSketchSeg = swSketch.GetSketchSegments

         For i = 0 To UBound(vSketchSeg)
             swSketchSeg = vSketchSeg(i)
             swSketchSeg.Select4(True, Nothing)
         Next

         ' Create a chain using the selected sketch segments
         bRet = swSketchMgr.MakeSketchChain
         swModel.ClearSelection2(True)

         ' Get the sketch path
         vSketchPath = swSketch.GetSketchPaths
         swModel.ClearSelection2(True)

         ' Create a circle
         swSketchMgr.CreateCircle(-0.07515069296375, 0.04810565031983, 0, -0.055655, 0.037535, 0)

         ' Add a tangent relation between sketch path and sketch circle
         boolstatus = swModel.Extension.SelectByID2("Arc1", "SKETCHSEGMENT", -0.0544261072733269, 0.0471088420855688, -0.00328513702299429, False, 0, Nothing, 0)
         boolstatus = swModel.Extension.SelectByID2("Line1", "SKETCHSEGMENT", -0.0422450565500339, 0.0367651345154678, -0.00268554920844266, True, 0, Nothing, 0)
         swModel.SketchAddConstraints("sgTANGENT")

         ' Print the number of constraints, number of relations,
         ' path length, number of sketch segments, whether the path was selected,
         ' type of constraints, and type of relations
         For i = 0 To UBound(vSketchPath)

             swSketchPath = vSketchPath(i)
             Debug.Print(" Number of constraints: " & swSketchPath.GetConstraintsCount)
             Debug.Print(" Number of relations: " & swSketchPath.GetRelationsCount)
             Debug.Print(" Path length: " & swSketchPath.GetLength)
             Debug.Print(" Number of segments: " & swSketchPath.GetSketchSegmentCount)
             Debug.Print(" Selection result: " & swSketchPath.Select(False, Nothing))

             vConstraint = swSketchPath.GetConstraints

             Dim j As Integer
             j = 0

             If (Not IsNothing(vConstraint)) Then
                 For j = 0 To UBound(vConstraint)
                     Debug.Print("  SketchSegConstraint[" & i & "]: " & vConstraint(j))
                 Next j
             End If

             vRelation = swSketchPath.GetRelations

             Dim k As Integer
             k = 0

             For Each vSkRel In vRelation
                 swSkRel = vSkRel
                 Debug.Print("    Relation(" & k & ")")
                 Debug.Print("      Type: " & swSkRel.GetRelationType)
                 k = k + 1
             Next

             ' Get the sketch segments in the sketch path and
             ' their lengths
             vSketchSeg = swSketchPath.GetSketchSegments

             Dim l As Integer
             For l = 0 To UBound(vSketchSeg)

                 swSketchSeg = vSketchSeg(l)

                 ' Ignore construction lines
                 If swSketchSeg.ConstructionGeometry = False Then
                     ' Ignore text
                     If swSketchSegments_e.swSketchTEXT <> swSketchSeg.GetType Then
                         nLength = nLength + swSketchSeg.GetLength
                     End If
                 End If

             Next l

             Debug.Print(" Total path length calculated by segment: " & nLength)

         Next

         swModel.SketchManager.InsertSketch(True)
     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
