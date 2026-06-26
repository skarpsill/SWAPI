---
title: "Get Model Pathnames from a BOM Table Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Model_Path_Names_in_BOM_Table_Example_VBNET.htm"
---

# Get Model Pathnames from a BOM Table Example (VB.NET)

This example shows how to get the model pathnames from a specified row of a BOM table annotation.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open a drawing containing a BOM table annotation named Bill of Materials1.
 ' 2. Open an Immediate Window.
 '
 ' Postconditions: Inspect the Immediate Window for model pathnames.
 ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub Main()

         Dim swModel As ModelDoc2
         Dim swDraw As DrawingDoc
         Dim swFeat As Feature
         Dim swBomFeat As BomFeature

         swModel = swApp.ActiveDoc
         swDraw = swModel
         swFeat = swModel.FirstFeature
         Do While Not swFeat Is  Nothing
             If (swFeat.GetTypeName = "BomFeat") Then
                 Debug.Print("******************************")
                 Debug.Print("Feature Name = " & swFeat.Name)
                 swBomFeat = swFeat.GetSpecificFeature2
                 If (swFeat.Name = "Bill of Materials1") Then
                     ProcessBomFeature(swApp, swModel, swBomFeat)
                 End If
             End If
             swFeat = swFeat.GetNextFeature
         Loop
     End Sub
     Sub ProcessBomFeature(ByVal swApp As SldWorks, ByVal swModel As ModelDoc2, ByVal swBomFeat As BomFeature)
         GetPathNames(swApp, swBomFeat)
     End Sub

     Sub GetPathNames(ByVal swApp As SldWorks, ByVal swBomFeature As BomFeature)
         Dim vConfigurations As Object
         Dim strConfiguration As String
         Dim vVisibility As Object = Nothing
         Dim lIdx As Long
         Dim lNumConfigurations As Long
         Dim lNumRow As Long
         Dim lNumColumn As Long
         Dim lRow As Long
         Dim swBOMTableAnnotation As BomTableAnnotation
         Dim swTableAnnotation As TableAnnotation
         Dim swDocument As ModelDoc2
         Dim swAssembly As AssemblyDoc
         Dim strDocumentName As String
         Dim lStartRow As Long
         Dim bGetVisible As Boolean
         Dim vModelPathNames As Object
         Dim strItemNumber As String = ""
         Dim strPartNumber As String = ""
         Dim vModelPathName As Object
         Dim strModelPathName As String

         strDocumentName = swBomFeature.GetReferencedModelName
         swDocument = swApp.GetOpenDocumentByName(strDocumentName)
         Debug.Print("Referenced model = " & strDocumentName)
         swAssembly = swDocument

         ' For now assume we have only 1 table annotation.
         swBOMTableAnnotation = swBomFeature.GetTableAnnotations(0)
         swTableAnnotation = swBOMTableAnnotation
         lNumRow = swTableAnnotation.RowCount
         lNumColumn = swTableAnnotation.ColumnCount

         lStartRow = 1

         If (Not (swTableAnnotation.TitleVisible = False)) Then
             lStartRow = 2
         End If

         bGetVisible =  False
         Debug.Print("# configurations = " & swBomFeature.GetConfigurationCount(bGetVisible))
         vConfigurations = swBomFeature.GetConfigurations(bGetVisible, vVisibility)

         If (Not IsNothing(vConfigurations)) Then
             lNumConfigurations = UBound(vConfigurations) - LBound(vConfigurations) + 1
             For lIdx = 0 To (lNumConfigurations - 1)
                 strConfiguration = vConfigurations(lIdx)
                 Debug.Print("")
                 Debug.Print("Configuration: " & strConfiguration)

                 For lRow = lStartRow To (lNumRow - 1)
                     Debug.Print("  row = " & (lRow - lStartRow + 1))
                     vModelPathNames = swTableAnnotation.GetModelPathNames(lRow, strItemNumber, strPartNumber)

                     Debug.Print("    item number = " & strItemNumber)
                     Debug.Print("    part number = " & strPartNumber)

                     If (Not IsNothing(vModelPathNames)) Then
                         Debug.Print("    # models contributing to row = " & swTableAnnotation.GetModelPathNamesCount(lRow))
                         For Each vModelPathName In vModelPathNames
                             strModelPathName = vModelPathName
                             Debug.Print("       " & strModelPathName)
                         Next vModelPathName
                     Else
                         Debug.Print("    # models contributing to row = 0")
                         Debug.Assert(False)
                     End If
                 Next lRow
             Next lIdx
         End If
     End Sub

     Public swApp As SldWorks

 End  Class
```
