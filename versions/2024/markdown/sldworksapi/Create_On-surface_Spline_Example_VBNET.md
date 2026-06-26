---
title: "Create On-surface Spline Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_On-surface_Spline_Example_VBNET.htm"
---

# Create On-surface Spline Example (VB.NET)

This example shows how to create a spline constrained to a surface.

```vb
  '----------------------------------------------------------------------------
 ' Preconditions: Open public_documents\samples\tutorial\api\cstick.sldprt.
 '
 ' Postconditions:
 ' 1. Creates a 3D sketch of a spline on a face.
 ' 2. Inspect the graphics area.
 '
  ' NOTE: Because the model is used elsewhere, do not save changes.
  '----------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices

 Partial Class SolidWorksMacro

     Dim swCurFace As Face2
     Dim swSelMgr As SelectionMgr
     Dim Part As ModelDoc2
     Dim skSegment As SketchSegment
     Dim pointArray As Object
     Dim points(11) As Double
     Dim surfs(0) As Object
     Dim surfaceArr(0) As Surface
     Dim selType As Integer
     Dim surfaceArrUbound As Integer
     Dim statuses(3) As Boolean
     Dim boolstatus As Boolean

     Sub main()

         Part = swApp.ActiveDoc

         points(0) = -0.0334270787209949
         points(1) = 0.0223913424029847
         points(2) = 0.053671471463652
         points(3) = 0.0153063989576147
         points(4) = 0.0478899892864157
         points(5) = 0.0250019220828396
         points(6) = 0.0511644715447442
         points(7) = 0.0272060072570875
         points(8) = 0.00578476387745854
         points(9) = 0.00259263831071606
         points(10) = 0.0262831648993199
         points(11) = -0.053206707614433
         pointArray = points

         boolstatus = Part.Extension.SelectByRay(0.030303902514845, 0.0286262382667246, 0.0385109058888133, -0.577381545199981, -0.577287712085548, -0.577381545199979, 0.00178932209693826, 2, False, 0, 0)

         swSelMgr = Part.SelectionManager

         selType = swSelMgr.GetSelectedObjectType3(1, -1)
         surfaceArrUbound = -1
         If selType = swSelectType_e.swSelFACES Then
             swCurFace = swSelMgr.GetSelectedObject6(1, -1)
             surfaceArrUbound = surfaceArrUbound + 1
             surfaceArr(surfaceArrUbound) = swCurFace.GetSurface()
         End If

         surfs = surfaceArr

         Dim dispArray() As DispatchWrapper
         dispArray = ObjectArrayToDispatchWrapperArray(surfaceArr)

         'Set the Direction parameter to an array of null DispatchWrappers
         'to use the view vector of the current view to project the points in pointArray
         'onto the surface in dispArray
         Dim dirArray As DispatchWrapper
         dirArray = New DispatchWrapper(Nothing)
         skSegment = Part.SketchManager.CreateSpline3((pointArray), dispArray, dirArray, True, statuses)
         Part.SketchManager.InsertSketch(True)

     End Sub
     Function ObjectArrayToDispatchWrapperArray(ByVal Objects As Surface()) As DispatchWrapper()
         Dim ArraySize As Integer
         ArraySize = Objects.GetUpperBound(0)
         Dim d(ArraySize) As DispatchWrapper
         Dim ArrayIndex As Integer
         For ArrayIndex = 0 To ArraySize
             d(ArrayIndex) = New DispatchWrapper(Objects(ArrayIndex))
         Next
         Return d
     End Function

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
