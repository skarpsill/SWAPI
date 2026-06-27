---
title: "Get Sketch Contours Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Contours_Example_VBNET.htm"
---

# Get Sketch Contours Example (VB.NET)

This example shows how to get the sketch contours in a model document.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains a Sketch1 feature.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the number of sketch contours in Sketch1 and whether
'    they are open or closed.
' 2. Gets the number of sketch segments in Sketch1 and their type.
' 3. Gets the number of edges Sketch1.
' 4. Examine the Immediate window.
'----------------------------------------------------------------------------

	Imports SolidWorks.Interop.sldworks

	Imports SolidWorks.Interop.swconst

	Imports System.Runtime.InteropServices

	Imports System

	Imports System.Diagnostics

	Partial Class SolidWorksMacro

	    Sub main()

	        Dim myModel As ModelDoc2

	        Dim myPart As PartDoc

	        Dim SelMgr As SelectionMgr

	        Dim mySelectData As SelectData

	        Dim myFeature As Feature

	        Dim mySketch As Sketch

	        Dim contourCount As Integer

	        Dim vSkContours As Object

	        Dim skContour As SketchContour

	        Dim vEdges As Object, myEdge As Edge

	        Dim skSegCount As Integer

	        Dim vSkSegments As Object

	        Dim skSegment As SketchSegment

	        Dim skSegType As Integer, skSegTypesString As String = Nothing

	        Dim closed As Boolean, closedString As String

	        Dim i As Integer, j As Integer, k As Integer

	        Dim boolstatus As Boolean

	        myModel = swApp.ActiveDoc

	        SelMgr = myModel.SelectionManager

	        mySelectData = SelMgr.CreateSelectData

	        myPart = myModel

	        myFeature = myPart.FeatureByName("Sketch1")

	        mySketch = myFeature.GetSpecificFeature2()

	        '             or

	        '    Set mySketch = myModel.GetActiveSketch2()

	        '    Set myFeature = mySketch

	        If Not mySketch Is Nothing Then

	            vSkContours = mySketch.GetSketchContours()

	            contourCount = UBound(vSkContours) - LBound(vSkContours) + 1

	            Debug.Print("")

	            Debug.Print(contourCount & "
	Contours in sketch " & myFeature.Name)

	            For i = LBound(vSkContours) To UBound(vSkContours)

	                skContour = vSkContours(i)

	                If Not skContour Is Nothing Then

	                    closed = skContour.IsClosed()

	                    If (closed = 0) Then

	                        closedString = "Open"

	                    Else

	                        closedString = "Closed"

	                    End If

	                    Debug.Print("  Contour
	" & i & ": " & closedString)

	                    vSkSegments = skContour.GetSketchSegments()

	                    skSegCount = UBound(vSkSegments) - LBound(vSkSegments) +
	1

	                    For j = LBound(vSkSegments) To UBound(vSkSegments)

	                        If j = LBound(vSkSegments) Then

	                            skSegTypesString = "("

	                        End If

	                        skSegment = vSkSegments(j)

	                        If Not skSegment Is Nothing Then

	                            skSegType = skSegment.GetType()

	                            Select Case skSegType

	                                Case swSketchSegments_e.swSketchLINE

	                                    skSegTypesString = skSegTypesString & "line"

	                                Case swSketchSegments_e.swSketchARC

	                                    skSegTypesString = skSegTypesString & "arc"

	                                Case swSketchSegments_e.swSketchELLIPSE

	                                    skSegTypesString = skSegTypesString & "ellipse"

	                                Case swSketchSegments_e.swSketchPARABOLA

	                                    skSegTypesString = skSegTypesString & "parabola"

	                                Case swSketchSegments_e.swSketchSPLINE

	                                    skSegTypesString = skSegTypesString & "spline"

	                                Case swSketchSegments_e.swSketchTEXT

	                                    skSegTypesString = skSegTypesString & "text"

	                                Case Nothing

	                                    skSegTypesString = skSegTypesString & "unknown"

	                            End Select

	                        End If

	                        If j = UBound(vSkSegments) Then

	                            skSegTypesString = skSegTypesString & ")"

	                        Else

	                            skSegTypesString = skSegTypesString & ","

	                        End If

	                    Next j

	                    Debug.Print("    Sketch
	segment count = " & skSegCount & " " & skSegTypesString)

	                    vEdges = skContour.GetEdges()

	                    If IsNothing(vEdges) Then

	                        Debug.Print("    No
	edges.")

	                    Else

	                        For k = LBound(vEdges) To UBound(vEdges)

	                            myEdge = vEdges(k)

	                            If Not myEdge Is Nothing Then

	                                Debug.Print("    Edge
	" & k & ": ")

	                            End If

	                        Next k

	                    End If

	                    boolstatus = skContour.Select2(False, mySelectData)

	                    If boolstatus = 0 Then

	                        Debug.Print("    Selection
	of contour failed.")

	                    End If

	                    Stop

	                End If

	            Next i

	        End If

	    End Sub

	    Public swApp As SldWorks

	End Class
```
