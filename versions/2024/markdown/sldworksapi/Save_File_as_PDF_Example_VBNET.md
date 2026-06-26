---
title: "Save File as PDF Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Save_File_as_PDF_Example_VBNET.htm"
---

# Save File as PDF Example (VB.NET)

This example shows how to save multiple drawing sheets to a PDF file.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Verify that the specified drawing document to open exists.
 ' 2. Verify that c:\test, the folder where to save
 '    the PDF file, exists. If it does not exist,
 '    create it or change the path to a folder that
 '    exists on your system.
 '
 ' Postconditions:
 ' 1. Opens the specified drawing document.
 ' 2. Saves all but the last drawing sheet to an array.
 ' 3. Saves the array of drawing sheets to a PDF file
 '    called foodprocessor.pdf.
 ' 4. Opens foodprocessor.pdf.
 '----------------------------------------------------------------------------

 Imports System.Runtime.InteropServices
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Public Sub main()

         Dim swExportPDFData As ExportPdfData
         Dim swModel As ModelDoc2
         Dim swModExt As ModelDocExtension
         Dim swDrawDoc As DrawingDoc
         Dim boolstatus As Boolean
         Dim filename As String
         Dim errors As Integer
         Dim warnings As Integer
         Dim objs() As Object
         Dim obj As Object

         ' Save PDF file to this folder and filename
         filename =  "c:\test\foodprocessor.pdf"

         ' Open drawing document
         swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
         swModExt = swModel.Extension
         swExportPDFData = swApp.GetExportFileData(swExportDataFileType_e.swExportPdfData)

         ' Get the names of the drawing sheets in the drawing
         ' to get the size of the array of drawing sheets
         swDrawDoc = swModel
         obj = swDrawDoc.GetSheetNames

         Dim count As Integer
         count = UBound(obj)
         ReDim objs(count)
          Dim arrObjIn(count) As DispatchWrapper

         Dim i As  Integer
         ' Activate each drawing sheet, except the last drawing sheet, for
         ' demonstration purposes only and add each sheet to an array
         ' of drawing sheets
         For i = 0 To count - 1
             boolstatus = swDrawDoc.ActivateSheet(obj(i))
             Dim swSheet As Sheet
             swSheet = swDrawDoc.GetCurrentSheet
             objs(i) = swSheet
              arrObjIn(i) = New DispatchWrapper(objs(i))
         Next i

         ' Save the drawings sheets to a PDF file
         boolstatus = swExportPDFData.SetSheets(swExportDataSheetsToExport_e.swExportData_ExportSpecifiedSheets, (arrObjIn))
         swExportPDFData.ViewPdfAfterSaving =  True
         Debug.Print(swExportPDFData.ViewPdfAfterSaving)
         boolstatus = swModExt.SaveAs(filename, swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, swExportPDFData, errors, warnings)

     End Sub

     Public swApp As SldWorks

 End  Class
```
