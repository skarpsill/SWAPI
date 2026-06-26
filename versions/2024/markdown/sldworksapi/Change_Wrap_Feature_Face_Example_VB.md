---
title: "Change Wrap Feature Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Wrap_Feature_Face_Example_VB.htm"
---

# Change Wrap Feature Face Example (VBA)

This example shows how to insert a wrap feature and change the face on which to apply a wrap feature.

```
'------------------------------------------------------------------------
' Preconditions: Verify that the part to open exists.
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
'------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swFeatureManager As SldWorks.FeatureManager
Dim swModelView As SldWorks.ModelView
Dim swWrapFeature As SldWorks.Feature
Dim swWrapFeatureData As SldWorks.WrapSketchFeatureData
Dim swSelectionManager As SldWorks.SelectionMgr
Dim swFace As SldWorks.Face2
Dim sketchLines As Variant
Dim status As Boolean
Dim errors As Long, warnings As Long
Dim fileName As String
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    ' Open part document
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\clamp1.sldprt"
    Set swModel = swApp.OpenDoc6(fileName, swDocPART, swOpenDocOptions_Silent, "", errors, warnings)
    Set swModelDocExt = swModel.Extension
```

```
    ' Sketch a rectangle on the top plane
    swModel.ShowNamedView2 "*Top", 5
    status = swModelDocExt.SelectByID2("Top Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchManager = swModel.SketchManager
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    swModel.ViewZoomtofit2
    sketchLines = swSketchManager.CreateCornerRectangle(-1.69758295694522E-03, 9.48506512727088E-04, 0, 1.3668226995581E-03, -9.84987532447629E-04, 0)
    swModel.ClearSelection2 True
```

```
    swSketchManager.InsertSketch True
    swModel.ClearSelection2 True
```

```
    ' Select the sketch of the rectangle and the
    ' face where to scribe the sketch as a wrap feature
    status = swModelDocExt.SelectByID2("Sketch11", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    status = swModelDocExt.SelectByID2("", "FACE", 3.03698880696047E-03, 0.036653462145523, -1.43855543627342E-03, True, 1, Nothing, 0)
```

```
    ' Insert the wrap feature
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.InsertWrapFeature(2, 0.001, False)
    swModel.ClearSelection2 True
```

```
    ' Rotate the part about its center to select another face
    Set swModelView = swModel.ActiveView
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 0.039572760932108, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 5.08792640555675E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 5.08792640555675E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 0.039572760932108, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.08792640555675E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 0.039572760932108, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 5.08792640555675E-02, -1.69162681347143E-02
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.08792640555675E-02, 0
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 9.61052765494052E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 0.039572760932108, 0
    swModelView.RotateAboutCenter 6.78390187407566E-02, 0
    swModelView.RotateAboutCenter 6.21857671790269E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 5.08792640555675E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 2.26130062469189E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 3.39195093703783E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, -8.45813406735716E-03
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.82662578086486E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 2.26130062469189E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.69597546851892E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, -8.45813406735716E-03
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 1.13065031234594E-02, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
    swModelView.RotateAboutCenter 5.65325156172972E-03, 0
```

```
    ' Select another face where to apply the wrap feature
    status = swModelDocExt.SelectByID2("", "FACE", 2.39269080197957E-03, 2.63524999999731E-02, -4.79719888705432E-04, True, 0, Nothing, 0)
    Set swSelectionManager = swModel.SelectionManager
    Set swFace = swSelectionManager.GetSelectedObject6(1, -1)
```

```
    ' Edit the wrap feature to wrap the rectangular
    ' sketch on the second face
    Set swWrapFeature = swModel.FeatureByName("Wrap1")
    Set swWrapFeatureData = swWrapFeature.GetDefinition
    status = swWrapFeatureData.AccessSelections(swModel, Nothing)
    swWrapFeatureData.Face = swFace
    Debug.Print "Wrap type: " & swWrapFeatureData.Type
    Debug.Print "Wrap thickness: " & swWrapFeatureData.Thickness
    Debug.Print "Reverse direction? " & swWrapFeatureData.ReverseDirection
    status = swWrapFeature.ModifyDefinition(swWrapFeatureData, swModel, Nothing)
```

```
    swModel.ClearSelection2 True
```

```
End Sub
```
