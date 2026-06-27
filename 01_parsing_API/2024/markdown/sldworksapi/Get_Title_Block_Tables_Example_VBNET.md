---
title: "Get Title Block Tables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Title_Block_Tables_Example_VBNET.htm"
---

# Get Title Block Tables Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Dim Part As ModelDoc2
    Dim tbtAnno As TitleBlockTableAnnotation
    Dim anno As TitleBlockTableAnnotation
    Dim tabannoObject As TitleBlockTableAnnotation
    Dim feat As TitleBlockTableFeature
    Dim tabfeatObject As TitleBlockTableFeature
    Dim annos As Object
    Dim I As Integer
    Dim selMgr As SelectionMgr
    Dim boolstatus As Boolean

    Sub main()

        Part = swApp.ActiveDoc
        Debug.Print("Inserting a title block table into the model using a general table template (*.sldtbt)")
        Debug.Print("")
        tbtAnno = Part.Extension.InsertTitleBlockTable("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\lang\english\connector-table.sldtbt", 500, 500)
        feat = tbtAnno.TitleBlockTableFeature
        Debug.Print("Title block table feature: " + feat.GetFeature.Name)
        Dim count As String
        count = feat.GetTableAnnotationCount
        Debug.Print("Title block table annotation count: " + count)
        Debug.Print("Title block table annotations")
        annos = feat.GetTableAnnotations
        For I = 0 To UBound(annos)
            anno = annos(I)
            Debug.Print("   Title block table feature: " + anno.TitleBlockTableFeature.GetFeature.Name)
        Next
        Debug.Print("")

        Debug.Print("Selecting title block table feature through IModelDocExtension::SelectByID2 type, TITLEBLOCKTABLEFEAT")
        boolstatus = Part.Extension.SelectByID2(feat.GetFeature.Name, "TITLEBLOCKTABLEFEAT", 0, 0, 0, False, 0, Nothing, 0)
        Debug.Print("  Casting selected object to ITitleBlockTableFeature")
        selMgr = Part.SelectionManager
        tabfeatObject = selMgr.GetSelectedObject6(1, -1)
        Debug.Print("     Title block table feature: " + tabfeatObject.GetFeature.Name)
        Debug.Print("")

        Debug.Print("Selecting title block table annotation through IModelDocExtension::SelectByID2 type, ANNOTATIONTABLES")
        boolstatus = Part.Extension.SelectByID2("DetailItem1@Annotations", "ANNOTATIONTABLES", -0.1205280774849, -0.01199819470702, 0.04087038255709, False, 0, Nothing, 0)
        Debug.Print("")
        Debug.Print("  Casting selected object to ITitleBlockTableAnnotation type")
        tabannoObject = selMgr.GetSelectedObject6(1, -1)
        Debug.Print("    Getting title block table feature from the title block table annotation")
        Debug.Print("       Title block table feature: " + tabannoObject.TitleBlockTableFeature.GetFeature.Name)
        Debug.Print("")

        Debug.Print("  Casting selected object to ITableAnnotation type")
        Dim annoObject As ITableAnnotation
        annoObject = selMgr.GetSelectedObject6(1, -1)
        Dim annoType As String
        annoType = annoObject.Type
        If annoType = swTableAnnotationType_e.swTableAnnotation_TitleBlock Then
            Debug.Print("     The selected table annotation is defined in swTableAnnotationType_e as TitleBlock")
        Else
            Debug.Print("     The selected table annotation is defined in swTableAnnotationType_e with value:   " + annoType)
        End If

    End Sub

    Public swApp As SldWorks

End Class
```
