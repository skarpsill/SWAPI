---
title: "Get Drawing Sheets Properties (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "swdocmgrapi/Get_Drawing_Sheets_Properties_Example_vbnet.htm"
---

# Get Drawing Sheets Properties (VB.NET)

## Get Drawing Sheets' Properties Example (VB.NET)

This example shows how to get the properties of a drawing's sheets.

```vb
'---------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Read the SOLIDWORKS Document Manager API Getting Started topic
 '    and ensure that the required DLLs are registered.
  ' 2. Copy and paste this code into a VB.NET console application
 '    in Microsoft Visual Studio.
 ' 3. Add the SolidWorks.Interop.swdocumentmgr.dll reference
 '    to the project:
 '    a. Right-click the solution in Solution Explorer.
 '    b. Click Add Reference.
 '    c. Click Browse.
 '    d. Click:
 '       install_dir\api\redist\SolidWorks.Interop.swdocumentmgr.dll
 ' 4. Ensure that the specified drawing document exists.
 ' 5. Open the Immediate window.
 ' 6. Substitute your_license_key with your SOLIDWORKS Document
 '    Manager license key.
 ' 7. Run the macro.
 '
 ' Postconditions: Examine the Immediate window.
'---------------------------------------------------------------------------
```

```vb
 Imports SolidWorks.Interop.swdocumentmgr
 Imports System.Runtime.InteropServices
 Imports System
 Imports SolidWorks.Interop
 Imports System.Diagnostics
 Imports System.Math

 Module Module1

     Sub Main()
         Dim swClassFact As SwDocumentMgr.SwDMClassFactory
         Dim docMgrApp As SwDocumentMgr.SwDMApplication
         Dim docDrw As SwDocumentMgr.SwDMDocument13
         Dim res As SwDocumentMgr.SwDmDocumentOpenError

         swClassFact = CreateObject("SwDocumentMgr.SwDMClassFactory")
         docMgrApp = swClassFact.GetApplication("your_license_key")
         docDrw = docMgrApp.GetDocument("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw", SwDmDocumentType.swDmDocumentDrawing, True, res)
         Dim sheetNameVar As Object
         Dim sheetCount As Integer

         sheetCount = docDrw.GetSheetCount
         sheetNameVar = docDrw.GetSheetNames

         Dim sheetName As String
         Dim sheetNameCount As Integer

         For sheetNameCount = LBound(sheetNameVar) To UBound(sheetNameVar)

             Dim formatName As String = ""
             Dim status1 As swdocumentmgr.swSheetFormatPathResult

             sheetName = sheetNameVar(sheetNameCount)
             status1 = docDrw.GetSheetFormatPath(sheetName, formatName)

             Debug.Print(sheetName & " ---- " & formatName & vbNewLine)

             Dim status2 As swdocumentmgr.swSheetPropertiesResult
             Dim formatProp As New Object

             status2 = docDrw.GetSheetProperties(sheetName, formatProp)

             Dim para As Double

             para = Round(formatProp(0), 1)

             Dim paperSize As String = ""

             GetPaperSize(para, paperSize)

             Debug.Print("Paper Size = " & paperSize)
             Debug.Print("Size = " & formatProp(1) & " x " & formatProp(2))
             Debug.Print("Scale = " & formatProp(3) & " : " & formatProp(4))

             Dim boolData As Boolean

             boolData = False

             If (formatProp(5) = 1) Then
                 boolData = True
             End If

             Debug.Print("First angle = " & boolData)

             Dim templateSize As String = ""

             para = Round(formatProp(6), 1)

             GetTemplateSize(para, templateSize)

             Debug.Print("Template size = " & templateSize)

             boolData = False

             If (formatProp(7) = 1) Then
                 boolData = True
             End If

             Debug.Print("Template visible = " & boolData)
             Debug.Print("===========================================")

         Next

         docDrw.CloseDoc()

     End Sub

     Sub GetPaperSize(ByVal inpNum As Double, ByRef outPaperType As String)

         If (inpNum = 0) Then

             outPaperType = "swDwgPaperAsize"

         ElseIf (inpNum = 1) Then

             outPaperType = "swDwgPaperAsizeVertical"

         ElseIf (inpNum = 2) Then

             outPaperType = "swDwgPaperBsize"

         ElseIf (inpNum = 3) Then

             outPaperType = "swDwgPaperCsize"

         ElseIf (inpNum = 4) Then

             outPaperType = "swDwgPaperDsize"

         ElseIf (inpNum = 5) Then

             outPaperType = "swDwgPaperEsize"

         ElseIf (inpNum = 6) Then

             outPaperType = "swDwgPaperA4size"

         ElseIf (inpNum = 7) Then

             outPaperType = "swDwgPaperA4sizeVertical"

         ElseIf (inpNum = 8) Then

             outPaperType = "swDwgPaperA3size"

         ElseIf (inpNum = 9) Then

             outPaperType = "swDwgPaperA2size"

         ElseIf (inpNum = 10) Then

             outPaperType = "swDwgPaperA1size"

         ElseIf (inpNum = 11) Then

             outPaperType = "swDwgPaperA0size"

         ElseIf (inpNum = 12) Then

             outPaperType = "swDwgPapersUserDefined"

         End If

     End Sub

     Sub GetTemplateSize(ByVal inpNum As Double, ByRef outTemplateType As String)

         If (inpNum = 0) Then

             outTemplateType = "swDwgTemplateAsize"

         ElseIf (inpNum = 1) Then

             outTemplateType = "swDwgTemplateAsizeVertical"

         ElseIf (inpNum = 2) Then

             outTemplateType = "swDwgTemplateBsize"

         ElseIf (inpNum = 3) Then

             outTemplateType = "swDwgTemplateCsize"

         ElseIf (inpNum = 4) Then

             outTemplateType = "swDwgTemplateDsize"

         ElseIf (inpNum = 5) Then

             outTemplateType = "swDwgTemplateEsize"

         ElseIf (inpNum = 6) Then

             outTemplateType = "swDwgTemplateA4size"

         ElseIf (inpNum = 7) Then

             outTemplateType = "swDwgTemplateA4sizeVertical"

         ElseIf (inpNum = 8) Then

             outTemplateType = "swDwgTemplateA3size"

         ElseIf (inpNum = 9) Then

             outTemplateType = "swDwgTemplateA2size"

         ElseIf (inpNum = 10) Then

             outTemplateType = "swDwgTemplateA1size"

         ElseIf (inpNum = 11) Then

             outTemplateType = "swDwgTemplateA0size"

         ElseIf (inpNum = 12) Then

             outTemplateType = "swDwgTemplateCustom"

         ElseIf (inpNum = 13) Then

             outTemplateType = "swDwgTemplateNone"

         End If

     End Sub

 End Module
```
