---
title: "Get Sketch Regions Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketch_Regions_Example_VBNET.htm"
---

# Get Sketch Regions Example (VB.NET)

This example shows how to get the sketch regions in a sketch.

```
'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a model document that contains a Sketch1 feature with
'    one or more sketch regions.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets each sketch region.
' 2. Press F5 at each Stop statement.
' 3. Examine the Immediate window.
'----------------------------------------------------------------------------

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

	        Dim regionCount As Integer

	        Dim vSkRegions As Object

	        Dim skRegion As SketchRegion

	        Dim myLoop As Loop2

	        Dim edgeCount As Integer, vertexCount As Integer

	        Dim vEdges As Object, myEdge As Edge

	        Dim vVertices As Object, myVertex As Vertex

	        Dim vPoint As Object, X As Double, Y As Double, Z As Double

	        Dim outer As Boolean, strOuter As String

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

	            regionCount = mySketch.GetSketchRegionCount()

	            Debug.Print("")

	            Debug.Print(regionCount & "
	regions in sketch " & myFeature.Name)

	            vSkRegions = mySketch.GetSketchRegions()

	            For i = LBound(vSkRegions) To UBound(vSkRegions)

	                skRegion = vSkRegions(i)

	                If Not skRegion Is Nothing Then

	                    Debug.Print("  Region
	" & i & ":")

	                    j = 0

	                    myLoop = skRegion.GetFirstLoop()

	                    While Not myLoop Is Nothing

	                        edgeCount = myLoop.GetEdgeCount()

	                        vertexCount = myLoop.GetVertexCount()

	                        outer = myLoop.IsOuter()

	                        If outer = 0 Then

	                            strOuter = "Inner loop"

	                        Else

	                            strOuter = "Outer loop"

	                        End If

	                        Debug.Print("    Loop
	" & j & ": " & edgeCount & " edges, " & vertexCount & " vertices, " & strOuter)

	                        vEdges = myLoop.GetEdges()

	                        For k = LBound(vEdges) To UBound(vEdges)

	                            myEdge = vEdges(k)

	                            If Not myEdge Is Nothing Then

	                                Debug.Print("      Edge
	" & k & ": ")

	                            End If

	                        Next k

	                        vVertices = myLoop.GetVertices()

	                        For k = LBound(vVertices) To UBound(vVertices)

	                            myVertex = vVertices(k)

	                            If Not myVertex Is Nothing Then

	                                vPoint = myVertex.GetPoint()

	                                X = vPoint(0)

	                                Y = vPoint(1)

	                                Z = vPoint(2)

	                                Debug.Print("      Vertex
	" & k & ": " & "(" & X & ", " & Y & ", " & Z
	& ")")

	                            End If

	                        Next k

	                        myLoop = myLoop.GetNext()

	                        j = j + 1

	                    End While

	                    boolstatus = skRegion.Select2(False, mySelectData)

	                    If boolstatus = 0 Then

	                        Debug.Print("    Selection
	of region failed.")

	                    End If

	                    Stop

	                End If

	            Next i

	        End If

	    End Sub

	    Public swApp As SldWorks

	End Class
```
