---
title: "Cut Body and Keep All Bodies Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Cut_Body_and_Keep_All_Bodies_Example_VBNET.htm"
---

# Cut Body and Keep All Bodies Example (VB.NET)

This example shows how to cut a body and keep all bodies.

```
'----------------------------------------------------------------------------
' Preconditions:
'  1. Verify that the specified part document template exists.
'  2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a body.
' 3. Splits the body into two bodies.
' 4. Examine the graphics area and Immediate window.
'-----------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim boolstatus As Boolean
    Dim Feature As Feature
    Public WithEvents swPart As PartDoc

    Public Sub main()

        'Open new part document
        Part = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\part.prtdot", 0, 0, 0)

        'Set up event
        swPart = Part
        AttachEventHandlers()

        'Create body
        Call CreateBodiesAndSketch()
        boolstatus = Part.Extension.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
        Feature = Part.FeatureManager.FeatureCut3(True, False, False, swEndConditions_e.swEndCondThroughAll, swEndConditions_e.swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True, False, False, False, swStartConditions_e.swStartSketchPlane, 0, False)
        If (Feature Is Nothing) Then
            Debug.Print("No feature created.")
        End If

    End Sub

    Sub CreateBodiesAndSketch()
        'Create body
        boolstatus = Part.Extension.SelectByID2("Front Plane", "PLANE", -0.06869486923422, 0.06291203863612, -0.006492164309718, False, 0, Nothing, 0)
        Part.ClearSelection2(True)
        Part.SketchRectangle(-0.0424567617866, 0.0388405707196, 0, 0.05638579404467, -0.03750124069479, 0, 1)
        Part.ShowNamedView2("*Trimetric", 8)
        Part.ClearSelection2(True)
        boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        Part.FeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.12, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, False, False, 0, 0, False)
```

```
        Part.ClearSelection2(True)

        'Create sketch for cut feature
        boolstatus = Part.Extension.SelectByID2("", "FACE", -0.02909828822015, 0.03884057071963, 0.09843602253397, False, 0, Nothing, 0)
        Part.SketchManager.InsertSketch(True)
        Part.ClearSelection2(True)
        Dim vSkLines As Object
        vSkLines = Part.SketchManager.CreateCornerRectangle(-0.0628943705795, -0.07743122635196, 0, 0.1160562766823, -0.04532565168643, 0)
        Part.ClearSelection2(True)
        boolstatus = Part.Extension.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
        boolstatus = Part.Extension.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)

    End Sub

    Sub AttachEventHandlers()
        AttachSWEvents()
    End Sub

    Sub AttachSWEvents()
        AddHandler swPart.PromptBodiesToKeepNotify, AddressOf Me.swPart_PromptBodiesToKeepNotify
    End Sub

    Private Function swPart_PromptBodiesToKeepNotify(ByVal swFeat As Object, ByRef bodies As Object) As Integer
        Debug.Print("PartDoc_PromptBodiesToKeepNotify fired.")
        Dim theFeature As Feature
        If Not swFeat Is Nothing Then
            theFeature = swFeat
            Dim bodiesToKeep(0) As Object
            'Change BodyOption to Body1 or Body2 to show other options
            Dim BodyOption As String
            BodyOption = "AllBodies"
            Select Case BodyOption
                Case "AllBodies"
                    theFeature.SetBodiesToKeep(True, bodiesToKeep, swInConfigurationOpts_e.swThisConfiguration, Nothing)
                Case "Body1"
                    bodiesToKeep(0) = bodies(0)
                    theFeature.SetBodiesToKeep(False, bodiesToKeep, swInConfigurationOpts_e.swThisConfiguration, Nothing)
                Case "Body2"
                    bodiesToKeep(0) = bodies(1)
                    theFeature.SetBodiesToKeep(False, bodiesToKeep, swInConfigurationOpts_e.swThisConfiguration, Nothing)
            End Select
        End If

    End Function

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
