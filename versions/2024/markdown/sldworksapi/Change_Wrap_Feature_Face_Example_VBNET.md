---
title: "Change Wrap Feature Face Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Wrap_Feature_Face_Example_VBNET.htm"
---

# Change Wrap Feature Face Example (VB.NET)

This example shows how to insert a wrap feature and change the face on which to apply a wrap feature.

```
'--------------------------------------------------------------------------
' Preconditions: Verify that the part document to open exists.
'
' Postconditions:
' 1. Opens the part document.
' 2. Sketches a rectangle on the top plane.
' 3. Selects the sketch of the rectangle and the
'    face where to scribe the sketch as a wrap feature.
' 4. Inserts the wrap feature.
' 5. Rotates the part about its center.
' 6. Selects another face on the part.
' 7. Edits the wrap feature and wraps the rectangular
'    sketch on the second face.
'
' NOTE: Because the part document is used elsewhere, do not save changes.
'--------------------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swFeature As Feature
        Dim swFeatureManager As FeatureManager
        Dim swModelView As ModelView
        Dim swWrapFeature As Feature
        Dim swWrapFeatureData As WrapSketchFeatureData
        Dim swSelectionManager As SelectionMgr
        Dim swFace As Face2
        Dim sketchLines As Object
        Dim status As Boolean
        Dim errors As Integer, warnings As Integer
        Dim fileName As String

        ' Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
        swModelDocExt = swModel.Extension

        ' Sketch a rectangle on the top plane
        swModel.ShowNamedView2("*Top", 5)
        status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
        swSketchManager = swModel.SketchManager
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)
        swModel.ViewZoomtofit2()
        sketchLines = swSketchManager.CreateCornerRectangle(-0.00169758295694522, 0.000948506512727088, 0, 0.0013668226995581, -0.000984987532447629, 0)
        swModel.ClearSelection2(True)
        swSketchManager.InsertSketch(True)
        swModel.ClearSelection2(True)

        ' Select the sketch of the rectangle and the
        ' face where to scribe the sketch as a wrap feature
        status = swModelDocExt.SelectByID2("Sketch11", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
        status = swModelDocExt.SelectByID2("", "FACE", 3.03698880696047E-03, 0.036653462145523, -1.43855543627342E-03, True, 1, Nothing, 0)

        ' Insert the wrap feature
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.InsertWrapFeature(2, 0.001, False)
        swModel.ClearSelection2(True)

        ' Rotate the part about its center to select another face
        swModelView = swModel.ActiveView
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.039572760932108, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0508792640555675, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.039572760932108, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.039572760932108, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0508792640555675, -0.0169162681347143)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0508792640555675, 0)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0961052765494052, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.039572760932108, 0)
        swModelView.RotateAboutCenter(0.0678390187407566, 0)
        swModelView.RotateAboutCenter(0.0621857671790269, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0508792640555675, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0226130062469189, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0339195093703783, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0282662578086486, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0226130062469189, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0169597546851892, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, -0.00845813406735716)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.0113065031234594, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)
        swModelView.RotateAboutCenter(0.00565325156172972, 0)

        ' Select another face where to apply the wrap feature
        status = swModelDocExt.SelectByID2("", "FACE", 0.00239269080197957, 0.0263524999999731, -0.000479719888705432, True, 0, Nothing, 0)
        swSelectionManager = swModel.SelectionManager
        swFace = swSelectionManager.GetSelectedObject6(1, -1)

        ' Edit the wrap feature to wrap the rectangular
        ' sketch on the second face
        swWrapFeature = swModel.FeatureByName("Wrap1")
        swWrapFeatureData = swWrapFeature.GetDefinition
        status = swWrapFeatureData.AccessSelections(swModel, Nothing)
        swWrapFeatureData.Face = swFace
        Debug.Print "Wrap type: " & swWrapFeatureData.Type
        Debug.Print "Wrap thickness: " & swWrapFeatureData.Thickness
        Debug.Print "Reverse direction? " & swWrapFeatureData.ReverseDirection
        status = swWrapFeature.ModifyDefinition(swWrapFeatureData, swModel, Nothing)
        swModel.ClearSelection2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
