---
title: "Get Model Pathnames from a BOM Table Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Path_Names_in_BOM_Table_Example_VB.htm"
---

# Get Model Pathnames from a BOM Table Example (VBA)

This example shows how to get the model pathnames from a specified row of a BOM table annotation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing containing a BOM table annotation named Bill of Materials1.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions: Inspect the Immediate Window for model pathnames.
 ' ---------------------------------------------------------------------------
Option Explicit
 Sub Main()
    Dim swApp       As SldWorks.SldWorks
     Dim swModel     As SldWorks.ModelDoc2
     Dim swDraw      As SldWorks.DrawingDoc
     Dim swFeat      As SldWorks.Feature
     Dim swBomFeat   As SldWorks.BomFeature

    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swDraw = swModel
     Set swFeat = swModel.FirstFeature
     Do While Not swFeat Is Nothing
         If (swFeat.GetTypeName = "BomFeat") Then
             Debug.Print "******************************"
             Debug.Print "Feature Name = " & swFeat.Name
             Set swBomFeat = swFeat.GetSpecificFeature2
             If (swFeat.Name = "Bill of Materials1") Then
                 ProcessBomFeature swApp, swModel, swBomFeat
             End If
         End If
         Set swFeat = swFeat.GetNextFeature
     Loop
 End Sub
 Sub ProcessBomFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swBomFeat As SldWorks.BomFeature)
     GetPathNames swApp, swBomFeat
 End Sub

Sub GetPathNames(swApp As SldWorks.SldWorks, ByVal swBomFeature As SldWorks.BomFeature)
     Dim vConfigurations               As Variant
     Dim strConfiguration              As String
     Dim vVisibility                   As Variant
     Dim lIdx                          As Long
     Dim lNumConfigurations            As Long
     Dim lNumRow                       As Long
     Dim lNumColumn                    As Long
     Dim lRow                          As Long
     Dim swBOMTableAnnotation          As SldWorks.BomTableAnnotation
     Dim swTableAnnotation             As SldWorks.TableAnnotation
     Dim swDocument                    As SldWorks.ModelDoc2
     Dim swAssembly                    As SldWorks.AssemblyDoc
     Dim strDocumentName               As String
     Dim lStartRow                     As Long
     Dim bGetVisible                   As Boolean
     Dim vModelPathNames               As Variant
     Dim strItemNumber                 As String
     Dim strPartNumber                 As String
     Dim vModelPathName                As Variant
     Dim strModelPathName              As String

    strDocumentName = swBomFeature.GetReferencedModelName
     Set swDocument = swApp.GetOpenDocumentByName(strDocumentName)
     Debug.Print "Referenced model = " & strDocumentName
     Set swAssembly = swDocument

    ' For now assume we have only 1 table annotation.
     Set swBOMTableAnnotation = swBomFeature.GetTableAnnotations(0)
     Set swTableAnnotation = swBOMTableAnnotation
     lNumRow = swTableAnnotation.RowCount
     lNumColumn = swTableAnnotation.ColumnCount

   lStartRow = 1

    If (Not (swTableAnnotation.TitleVisible = False)) Then
         lStartRow = 2
     End If

    bGetVisible = False
     Debug.Print "# configurations = " & swBomFeature.GetConfigurationCount(bGetVisible)
     vConfigurations = swBomFeature.GetConfigurations(bGetVisible, vVisibility)

    If (Not IsEmpty(vConfigurations)) Then
         lNumConfigurations = UBound(vConfigurations) - LBound(vConfigurations) + 1
         For lIdx = 0 To (lNumConfigurations - 1)
             strConfiguration = vConfigurations(lIdx)
             Debug.Print ""
             Debug.Print "Configuration: " & strConfiguration

            For lRow = lStartRow To (lNumRow - 1)
                 Debug.Print "  row = " & (lRow - lStartRow + 1)
                 vModelPathNames = swTableAnnotation.GetModelPathNames(lRow, strItemNumber, strPartNumber)

                Debug.Print "    item number = " & strItemNumber
                 Debug.Print "    part number = " & strPartNumber

                If (Not IsEmpty(vModelPathNames)) Then
                     Debug.Print "    # models contributing to row = " & swTableAnnotation.GetModelPathNamesCount(lRow)
                     For Each vModelPathName In vModelPathNames
                         strModelPathName = vModelPathName
                         Debug.Print "       " & strModelPathName
                     Next vModelPathName
                 Else
                     Debug.Print "    # models contributing to row = 0"
                     Debug.Assert (False)
                 End If
             Next lRow
         Next lIdx
     End If
 End Sub
```
