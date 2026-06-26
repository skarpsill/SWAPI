---
title: "Get BOM Tables Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_BOM_Tables_Example_VBNET.htm"
---

# Get BOM Tables Example (VB.NET)

This example shows how to get the BOM tables in a drawing document.

```vb
  '---------------------------------------------------------------------------
 ' Preconditions:
  ' 1. Create a console application using Visual Basic.
 ' 2. Verify that all output is redirected to the Immediate window. (In
 '    Visual Studio 2015, click Tools > Options > Debugging > General >
 '    Redirect all Output Window text to the Immediate Window).
 ' 3. Click Project > Add Reference > install_dir/api/redist/
 '     SolidWorks.Interop.swdocumentmgr.dll > OK.
 ' 4. Substitute your license key for your_license_key in the code.
 ' 5. Copy the specified drawing document to another file name.
 ' 6. Open the specified drawing document in SOLIDWORKS.
 ' 7. Ensure that both Bills of Materials are not hidden.
 ' 8. Save and rebuild the drawing.
 ' 9. Close SOLIDWORKS.
 '
 ' Postconditions: Prints to the Immediate window:
 ' * Document:
 '   * Path and file name
 '   * Last saved date
 ' * For each BOM table that is not hidden in the document:
 '   * Name
 '   * Whether hidden
 '   * Whether to display components with multiple configurations as one item
 '   * Part configuration grouping setting
 '   * Sheet name
 '   * Number of views on the sheet
 '   * Name of the custom property view for the sheet
 '
 ' NOTE: Restore the original drawing document, as it is used elsewhere.
  '---------------------------------------------------------------------------

 Imports SolidWorks.Interop.swdocumentmgr
 Imports System
 Imports System.Diagnostics

 Module Module1

     Dim dmClassFact As SwDMClassFactory
     Dim dmDocMgr As SwDMApplication3
     Dim dmDoc As ISwDMDocumen15
     Dim dmTable As ISwDMTable5
     Dim dmSheet As ISwDMSheet4
     Dim custPropView As ISwDMView
     Dim dmError As SwDmDocumentOpenError
     Dim arrviews As Array
     Dim nameDrawing As String

     Sub Main()

         dmClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         dmDocMgr = dmClassFact.GetApplication("your_license_key") 'Do not distribute
         nameDrawing = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2017\introsw\cabinet_bath.slddrw"

         'Get the SOLIDWORKS drawing document
         dmDoc = dmDocMgr.GetDocument(nameDrawing, SwDmDocumentType.swDmDocumentDrawing, False, dmError)
         Debug.Print("Document's full name: " & dmDoc.FullName)
         Debug.Print("Date document last saved: " & dmDoc.LastSavedDate)

         ' Get the names of the BOM tables that are not hidden in the SOLIDWORKS drawing document
         Dim tableNames As Object
         tableNames = dmDoc.GetTableNames(SwDmTableType.swDmTableTypeBOM)
         Dim i As Integer
         If Not IsNothing(tableNames) Then
             For i = 0 To UBound(tableNames)
                 dmTable = dmDoc.GetTable(tableNames(i))
                 Debug.Print(" BOM table name: " & dmTable.Name)
                 Debug.Print("   Is BOM table hidden? " & dmTable.Hidden)
                 Debug.Print("   If BOM table contains components with multiple configurations, display as one item? " & dmTable.DisplayAsOneItem)
                 Debug.Print("   Part configuration grouping as defined in swDMPartConfigurationGrouping:  " & dmTable.PartConfigurationGrouping)
                 dmSheet = dmTable.Sheet
                 If Not IsNothing(dmSheet) Then
                     custPropView = dmSheet.CustomPropertyView
                     arrviews = dmSheet.GetViews
                     Debug.Print("   On sheet: " & dmSheet.Name)
                     Debug.Print("   Number of views on sheet: " & arrviews.Length)
                     Debug.Print("   Custom property view: " & custPropView.Name)
                 End If
             Next
         End If
     End Sub
 End Module
```
