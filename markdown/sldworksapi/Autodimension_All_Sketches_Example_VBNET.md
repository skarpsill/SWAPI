---
title: "Autodimension All Sketches Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Autodimension_All_Sketches_Example_VBNET.htm"
---

# Autodimension All Sketches Example (VB.NET)

This example shows how to autodimension all under-constrained sketches in a part.

```
'------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Inserts two sketches.
' 3. Autodimensions the sketches.
' 4. Examine the Immediate window.
'-----------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro
    Const swTnProfileFeature As String = "ProfileFeature"
    Const nTolerance As Double = 0.00000001

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swPart As PartDoc
        Dim sketchLines As Object
        Dim sSketchNameArr() As String
        Dim sSketchName As Object
        Dim swFeat As Feature
        Dim swSketch As Sketch
        Dim sketchSegment As SketchSegment
        Dim swSketchMgr As SketchManager
        Dim nRetVal As Integer
        Dim bRet As Boolean

        swApp = CreateObject("SldWorks.Application")

        ' Create new part document and inserts sketches
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2015\templates\Part.prtdot", 0, 0, 0)
        swModelDocExt = swModel.Extension
        bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        swSketchMgr = swModel.SketchManager
        sketchLines = swSketchMgr.CreateCornerRectangle(0, 0, 0, 0.0711560575730914, -0.0480714437538268, 0)
        swModel.ClearSelection2(True)
        bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
        bRet = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
        sketchLines = swSketchMgr.CreateCornerRectangle(-0.100496797175254, 0.0481170506199078, 0, -0.0506046179404507, 0.0100165849869995, 0)
        swModel.ClearSelection2(True)
        sketchSegment = swSketchMgr.CreateCircle(-0.06189, -0.041869, 0.0#, -0.066641, -0.077213, 0.0#)
        swModel.ClearSelection2(True)
        swSketchMgr.InsertSketch(True)
	sketchSegment = swSketchMgr.CreateCircle(-0.032637, 0.106589, 0.0#, -0.021539, 0.095387, 0.0#)
	swModel.ClearSelection2(True)
	sketchSegment = swSketchMgr.CreateCircle(0.0#, 0.083617, 0.0#, 0.01255, 0.067729, 0.0#)
	swModel.ClearSelection2(True)
	swSketchMgr.InsertSketch(True)
	swModel.ClearSelection2(True)

	' Find all under-constrained sketches
	ReDim sSketchNameArr(0)
	swPart = swModel
	swFeat = swPart.FirstFeature
	Do While Not swFeat Is Nothing
		If swTnProfileFeature = swFeat.GetTypeName2 Then
			swSketch = swFeat.GetSpecificFeature2
			If swConstrainedStatus_e.swUnderConstrained = swSketch.GetConstrainedStatus Then
				sSketchNameArr(UBound(sSketchNameArr)) = swFeat.Name
				ReDim Preserve sSketchNameArr(UBound(sSketchNameArr) + 1)
			End If
		End If
		swFeat = swFeat.GetNextFeature
	Loop

	' Remove last empty sketch name
	ReDim Preserve sSketchNameArr(UBound(sSketchNameArr) - 1)

	'Autodimension under-constrained sketches
        For Each sSketchName In sSketchNameArr
            swFeat = swPart.FeatureByName(sSketchName)
            swSketch = swFeat.GetSpecificFeature2
            nRetVal = AutoDimensionSketch(swApp, swModel, swSketch)
            Debug.Print(sSketchName & " autodimensioned (0 = success): " & nRetVal)
        Next

    End Sub

    Function GetAllSketchLines(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSketch As Sketch) As Object
        Dim vSketchSegArr As Object
        Dim vSketchSeg As Object
        Dim swSketchSeg As SketchSegment
        Dim swSketchCurrLine As SketchLine
        Dim swSketchLineArr() As SketchLine

        ReDim swSketchLineArr(0)
        vSketchSegArr = swSketch.GetSketchSegments
        If Not IsNothing(vSketchSegArr) Then
            For Each vSketchSeg In vSketchSegArr
                swSketchSeg = vSketchSeg
                If swSketchSegments_e.swSketchLINE = swSketchSeg.GetType Then
                    swSketchCurrLine = swSketchSeg
                    swSketchLineArr(UBound(swSketchLineArr)) = swSketchCurrLine
                    ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) + 1)
                End If
            Next
        End If
        If 0 = UBound(swSketchLineArr) Then
            ' No straight lines in this sketch
            GetAllSketchLines = Nothing
            Exit Function
        End If
        ' Remove last empty sketch line
        ReDim Preserve swSketchLineArr(UBound(swSketchLineArr) - 1)
        GetAllSketchLines = swSketchLineArr
    End Function

    Function GetSketchPoint(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSketch As Sketch, ByVal swSketchPt As SketchPoint) As Boolean
        Dim vSketchPtArr As Object

        vSketchPtArr = swSketch.GetSketchPoints2
        If Not IsNothing(vSketchPtArr) Then
            ' Use first point
            swSketchPt = vSketchPtArr(0)
            GetSketchPoint = True
            Exit Function
        End If
        GetSketchPoint = False
    End Function

    Function FindVerticalOrigin(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSketch As Sketch, ByVal swSketchSegVert As SketchSegment, ByVal swSketchPtVert As SketchPoint) As Boolean
        Dim vSketchLineArr As Object
        Dim vSketchLine As Object
        Dim swSketchCurrLine As SketchLine
        Dim swStartPt As SketchPoint
        Dim swEndPt As SketchPoint

        ' Try to get first vertical line
        vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
        If Not IsNothing(vSketchLineArr) Then
            For Each vSketchLine In vSketchLineArr
                swSketchCurrLine = vSketchLine
                swStartPt = swSketchCurrLine.GetStartPoint2
                swEndPt = swSketchCurrLine.GetEndPoint2
                If Math.Abs(swStartPt.X - swEndPt.X) < nTolerance Then
                    swSketchSegVert = swSketchCurrLine
                    FindVerticalOrigin = True
                    Exit Function
                End If
            Next
        End If
        ' Try to get the first point
        FindVerticalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtVert)
    End Function

    Function FindHorizontalOrigin(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSketch As Sketch, ByVal swSketchSegHoriz As SketchSegment, ByVal swSketchPtHoriz As SketchPoint) As Boolean
        Dim vSketchLineArr As Object
        Dim vSketchLine As Object
        Dim swSketchCurrLine As SketchLine
        Dim swStartPt As SketchPoint
        Dim swEndPt As SketchPoint

        ' Try to get first horizontal line
        vSketchLineArr = GetAllSketchLines(swApp, swModel, swSketch)
        If Not IsNothing(vSketchLineArr) Then
            For Each vSketchLine In vSketchLineArr
                swSketchCurrLine = vSketchLine
                swStartPt = swSketchCurrLine.GetStartPoint2
                swEndPt = swSketchCurrLine.GetEndPoint2
                If Math.Abs(swStartPt.Y - swEndPt.Y) < nTolerance Then
                    swSketchSegHoriz = swSketchCurrLine
                    FindHorizontalOrigin = True
                    Exit Function
                End If
            Next
        End If
        ' Try to get the first point
        FindHorizontalOrigin = GetSketchPoint(swApp, swModel, swSketch, swSketchPtHoriz)
    End Function

    Function AutoDimensionSketch(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swSketch As Sketch) As Integer
        Dim swFeat As Feature
        Dim swSketchSegHoriz As SketchSegment = Nothing
        Dim swSketchPtHoriz As SketchPoint = Nothing
        Dim swSketchSegVert As SketchSegment = Nothing
        Dim swSketchPtVert As SketchPoint = Nothing
        Dim bRet As Boolean
	Dim swSketchMgr As SketchManager = Nothing

        If False = FindHorizontalOrigin(swApp, swModel, swSketch, swSketchSegHoriz, swSketchPtHoriz) Then
            AutoDimensionSketch = swAutodimStatus_e.swAutodimStatusDatumLineNotHorizontal
            Exit Function
        End If
        If False = FindVerticalOrigin(swApp, swModel, swSketch, swSketchSegVert, swSketchPtVert) Then
            AutoDimensionSketch = swAutodimStatus_e.swAutodimStatusDatumLineNotVertical
            Exit Function
        End If
        swFeat = swSketch
        bRet = swFeat.Select2(False, 0)
        ' Editing sketch clears selections
        swModel.EditSketch()
        ' Reselect sketch segments for autodimensioning
        If Not swSketchSegVert Is Nothing Then
            ' Vertical line is for horizontal datum
            bRet = swSketchSegVert.Select4(True, Nothing)
        ElseIf Not swSketchPtHoriz Is Nothing Then
            bRet = swSketchPtHoriz.Select4(True, Nothing)
        ElseIf Not swSketchPtVert Is Nothing Then
            ' Use any sketch point for horizontal datum
            bRet = swSketchPtVert.Select4(True, Nothing)
        End If
        If Not swSketchSegHoriz Is Nothing Then
            ' Horizontal line is for vertical datum
            bRet = swSketchSegHoriz.Select4(True, Nothing)
        ElseIf Not swSketchPtVert Is Nothing Then
            bRet = swSketchPtVert.Select4(True, Nothing)
        ElseIf Not swSketchPtHoriz Is Nothing Then
            ' Use any sketch point for vertical datum
            bRet = swSketchPtHoriz.Select4(True, Nothing)
        End If
        ' No straight lines, probably contains circles,
        ' so use sketch points for datums
        If IsNothing(GetAllSketchLines(swApp, swModel, swSketch)) Then
            If Not swSketchPtHoriz Is Nothing Then
                bRet = swSketchPtHoriz.Select4(False, Nothing)
            ElseIf Not swSketchPtVert Is Nothing Then
                bRet = swSketchPtVert.Select4(False, Nothing)
            End If
        End If
        AutoDimensionSketch = swSketch.AutoDimension2(swAutodimEntities_e.swAutodimEntitiesAll, swAutodimScheme_e.swAutodimSchemeBaseline, swAutodimHorizontalPlacement_e.swAutodimHorizontalPlacementBelow, swAutodimScheme_e.swAutodimSchemeBaseline, swAutodimVerticalPlacement_e.swAutodimVerticalPlacementLeft)
        ' Redraw so dimensions are displayed
        swModel.GraphicsRedraw2()
        ' Exit sketch mode
        swSketchMgr = swModel.SketchManager
        swSketchMgr.InsertSketch(False)
    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
