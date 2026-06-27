---
title: "Modify and Reload Sheet Format Template Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm"
---

# Modify and Reload Sheet Format Template Example (VB.NET)

This example shows how to modify and reload a sheet format template.

```
'------------------------------------------------------------
' Preconditions:
' 1. Make a copy of:
'    C:\ProgramData\SolidWorks\SOLIDWORKS version\lang\english\sheetformat\a0 - iso.slddrt.
' 2. Create a new blank drawing using standard sheet size AO (ISO).
' 3. Add another blank sheet to the drawing, for a total of two sheets.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Modifies the sheet format template to include a new
'    note.
' 2. Examine Sheet1, Sheet2, and the Immediate window.
' 3. Delete:
'    C:\ProgramData\SolidWorks\SOLIDWORKS version\lang\english\sheetformat\a0 - iso.slddrt.
' 4. Rename the copy that you made in Preconditions step 1 to:
'    C:\ProgramData\SolidWorks\SOLIDWORKS version\lang\english\sheetformat\a0 - iso.slddrt.
'------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Const TEST_APPLY_CHANGES_TO_ALL As Boolean = True

    Private Function GetReloadResult(ByVal result As swReloadTemplateResult_e) As String
        Select Case result
            Case swReloadTemplateResult_e.swReloadTemplate_Success
                GetReloadResult = "Success"
            Case swReloadTemplateResult_e.swReloadTemplate_UnknownError
                GetReloadResult = "FAIL - Unknown Error"
            Case swReloadTemplateResult_e.swReloadTemplate_FileNotFound
                GetReloadResult = "FAIL - File Not Found"
            Case swReloadTemplateResult_e.swReloadTemplate_CustomSheet
                GetReloadResult = "FAIL - Custom Sheet"
            Case swReloadTemplateResult_e.swReloadTemplate_ViewOnly
                GetReloadResult = "FAIL - View Only"
            Case Else
                GetReloadResult = "FAIL - <unrecognized error code - " & result & ">"
        End Select
    End Function

    Public Sub main()

        Dim swModel As ModelDoc2
        swModel = swApp.ActiveDoc

        If swModel Is Nothing Then
            Debug.Print("Create a new empty drawing and add a second sheet to the drawing.")
            Exit Sub
        End If

        If swModel.GetType <> swDocumentTypes_e.swDocDRAWING Then Exit Sub

        Dim swDrwng As DrawingDoc
        swDrwng = swModel

        'Get the current sheet
        Dim activeSheet As Sheet
        activeSheet = swDrwng.GetCurrentSheet
        Debug.Print("Active sheet name: " & activeSheet.GetName)

        'Get the sheet format template
        Dim templateName As String
        templateName = activeSheet.GetTemplateName()
        Debug.Print("Sheet format template name to modify: " & templateName)
        swDrwng.EditTemplate()

        'Add a new note to the sheet format template
        Dim swNote As Note
        swNote = swModel.InsertNote("A New Note")
        Dim swAnno As Annotation
        swAnno = swNote.GetAnnotation
        swAnno.SetPosition2(0, 0.2, 0)
        Dim txtFormat As TextFormat
        txtFormat = swAnno.GetTextFormat(0)
        txtFormat.BackWards = (txtFormat.BackWards = False)
        txtFormat.Bold = True
        txtFormat.CharHeightInPts = 10 * txtFormat.CharHeightInPts
        swAnno.SetTextFormat(0, False, txtFormat)
        swDrwng.EditSheet()

        'At this point, the active sheet's format has changed

        If TEST_APPLY_CHANGES_TO_ALL Then
            'Save sheet format back to original sheet format template
            activeSheet.SaveFormat(templateName)
            'Reload all other sheets from the updated sheet format template
            Dim vSheetNames As Object
            vSheetNames = swDrwng.GetSheetNames()
            Dim vName As Object
            For Each vName In vSheetNames
                If Not vName = activeSheet.GetName Then
                    Debug.Print("Other sheet name: " & vName)
                    Dim otherSheet As Sheet
                    otherSheet = swDrwng.Sheet(vName)
                    If otherSheet.GetTemplateName = templateName Then
                        Dim reloadResult As swReloadTemplateResult_e

                        'Keep modifications and and reload all other elements
                        'from original sheet format template
                        reloadResult = otherSheet.ReloadTemplate(True)

                        'Discard modifications and reload all elements from
                        'original sheet format template
                        'reloadResult = otherSheet.ReloadTemplate(False)

                        Debug.Print("Reload sheet format for <" & otherSheet.GetName & ">: " & GetReloadResult(reloadResult))

                    End If
                End If
            Next
            swDrwng.ActivateSheet(activeSheet.GetName)

        Else

            'Discard the changes and reload the original sheet format template
            Dim reloadResult As swReloadTemplateResult_e
            reloadResult = activeSheet.ReloadTemplate(False)
            Debug.Print("Done - " & GetReloadResult(reloadResult))

        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
