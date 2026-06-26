---
title: "Get Title Block Tables Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Title_Block_Tables_Example_VB6.htm"
---

# Get Title Block Tables Example (VBA)

This example shows how to get title block tables.

```
'-------------------------------------------------
' Preconditions:
' 1. Open a part that does not contain any annotations.
' 2. Verify that the specified table template exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Inspect the output in the Immediate window.
' 2. Observe the new title block table feature under Tables
'    in the FeatureManager design tree (if necessary, right-click the
'    part in the FeatureManager design tree, click Hidden Tree
'    Items > Hide/Show Tree Items > Show in the Tables drop-down list).
' 3. Observe the corresponding title block table annotation
'    in the graphics area.
'--------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim Part As SldWorks.ModelDoc2
Dim tbtAnno As SldWorks.TitleBlockTableAnnotation
Dim anno As SldWorks.TitleBlockTableAnnotation
Dim tabannoObject As SldWorks.TitleBlockTableAnnotation
Dim feat As SldWorks.TitleBlockTableFeature
Dim tabfeatObject As SldWorks.TitleBlockTableFeature
Dim annos As Variant
Dim I As Long
Dim selMgr As SldWorks.SelectionMgr
Dim boolstatus As Boolean

Sub main()
```

```
    Set swApp = Application.SldWorks
    Set Part = swApp.ActiveDoc
    Debug.Print "Inserting a title block table into the model using a general table template (*.sldtbt)"
    Debug.Print ""
```

```
    Set tbtAnno = Part.Extension.InsertTitleBlockTable("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\connector-table.sldtbt", 500, 500)
    Set feat = tbtAnno.TitleBlockTableFeature
    Debug.Print "Title block table feature: " + feat.GetFeature.Name
    Dim count As String
    count = feat.GetTableAnnotationCount
    Debug.Print "Title block table annotation count: " + count
    Debug.Print "Title block table annotations"
    annos = feat.GetTableAnnotations
    For I = 0 To UBound(annos)
        Set anno = annos(I)
        Debug.Print "   Title block table feature: " + anno.TitleBlockTableFeature.GetFeature.Name
    Next
    Debug.Print ""
```

```
    Debug.Print "Selecting title block table feature through IModelDocExtension::SelectByID2 type, TITLEBLOCKTABLEFEAT"
    boolstatus = Part.Extension.SelectByID2(feat.GetFeature.Name, "TITLEBLOCKTABLEFEAT", 0, 0, 0, False, 0, Nothing, 0)
    Debug.Print "  Casting selected object to ITitleBlockTableFeature"
    Set selMgr = Part.SelectionManager
    Set tabfeatObject = selMgr.GetSelectedObject6(1, -1)
    Debug.Print "     Title block table feature: " + tabfeatObject.GetFeature.Name
    Debug.Print ""
```

```
    Debug.Print "Selecting title block table annotation through IModelDocExtension::SelectByID2 type, ANNOTATIONTABLES"
    boolstatus = Part.Extension.SelectByID2("DetailItem1@Annotations", "ANNOTATIONTABLES", -0.1205280774849, -0.01199819470702, 0.04087038255709, False, 0, Nothing, 0)
    Debug.Print "  Casting selected object to ITitleBlockTableAnnotation type"
    Set tabannoObject = selMgr.GetSelectedObject6(1, -1)
    Debug.Print "    Getting title block table feature from the title block table annotation"
    Debug.Print "      Title block table feature: " + tabannoObject.TitleBlockTableFeature.GetFeature.Name
    Debug.Print ""
```

```
    Debug.Print "  Casting selected object to ITableAnnotation type"
    Dim annoObject As ITableAnnotation
    Set annoObject = selMgr.GetSelectedObject6(1, -1)
    Dim annoType As String
    annoType = annoObject.Type
    If annoType = swTableAnnotationType_e.swTableAnnotation_TitleBlock Then
        Debug.Print "     The selected table annotation is defined in swTableAnnotationType_e as TitleBlock"
    Else
        Debug.Print "     The selected table annotation is defined in swTableAnnotationType_e with value:   " + annoType
    End If
```

```
End Sub
```
