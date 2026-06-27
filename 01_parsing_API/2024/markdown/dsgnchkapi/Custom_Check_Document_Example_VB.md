---
title: "Custom Check Document (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "dsgnchkapi/Custom_Check_Document_Example_VB.htm"
---

# Custom Check Document (VBA)

This example shows how to find out if an isometric view exists within
a drawing document using SOLIDWORKS Design Checker Custom Check.

To run this macro, register the macro in SOLIDWORKS Design Checker Custom
Check, then check an active drawings document using SOLIDWORKS Design
Checker and the standards file in which the macro was stored.

```vb
'--------------------------------------
Dim nFailedItemCount As Integer
Dim bCheckStatus As Boolean
Dim swApp As SldWorks.SldWorks
Dim errorCode As Long

Sub Validate()

Set swApp = Application.SldWorks

' Validate document
bCheckStatus = True

Dim FailedItemsArr() As String
bCheckStatus = RunCheck(FailedItemsArr)

' Inform SOLIDWORKS Design Checker about the results
Dim dcApp As DesignCheckerLib.SWDesignCheck

' Get the SOLIDWORKS Design Checker add-in
 ' Recommended to use the version-specific ProgID for your version of Design Checker
 ' e.g., "SWDesignChecker.SWDesignCheck.yyyy"
 ' See the Remarks section in ISWDesignCheck help
Set dcApp = swApp.GetAddInObject("SWDesignChecker.SWDesignCheck")
errorCode = dcApp.SetCustomCheckResult(bCheckStatus, (FailedItemsArr))

End Sub

Function RunCheck(ByRef FailedItemsArr() As String) As Boolean

Dim Part As ModelDoc2
Dim pViews() As View
Dim SheetNames() As String
Dim CurrentActiveSheet As Sheet
Dim strCurrentActiveSheet As String
Dim strIsometric As String

' Every view's orientation is compared with *Isometric
strIsometric = "*Isometric"

On Error GoTo ON_ERROR
RunCheck = True ' Set check to passed state
nFailedItemCount = 0

Set swApp = Application.SldWorks
Set Part = swApp.ActiveDoc

Dim eDocType As swDocumentTypes_e
eDocType = Part.GetType
If eDocType = swDocDRAWING Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim pDrawingDoc As DrawingDoc
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set pDrawingDoc = Part
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim pView As View
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Remember current active sheet's name to activate it again later
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim strOriginallyActiveSheet As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}strOriginallyActiveSheet = CurrentActiveSheet.GetName
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Get sheet count
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim nSheetCount As Integer
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}nSheetCount = pDrawingDoc.GetSheetCount
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Set size of the array
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}ReDim Preserve SheetNames(nSheetCount) As String
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Activate first sheet
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Dim isFirstSheet As Boolean
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}isFirstSheet = False
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}While isFirstSheet = False
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strCurrentActiveSheet = CurrentActiveSheet.GetName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}pDrawingDoc.SheetPrevious
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim PrevSheet As Sheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim strPrevSheet As String
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Set PrevSheet = pDrawingDoc.GetCurrentSheet
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}strPrevSheet = PrevSheet.GetName
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}If strPrevSheet = strCurrentActiveSheet Then
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}isFirstSheet = True
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}Wend
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}' Loop through all sheets
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}If nSheetCount > 0 Then
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Dim nCount As Integer
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}For nCount = 1 To nSheetCount
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set CurrentActiveSheet = pDrawingDoc.GetCurrentSheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}strCurrentActiveSheet = CurrentActiveSheet.GetName
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}SheetNames(nSheetCount) = strCurrentActiveSheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Debug.Print strCurrentActiveSheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Variable to track if any *Isometric view found in sheet
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim IsIsometricViewPresent As Boolean
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Set to not found
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}IsIsometricViewPresent = False
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' Loop through all views
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim nViewCount As Integer
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}nViewCount = 0
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Dim pTempView As View
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Set pTempView = pDrawingDoc.GetFirstView
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}While (Not pTempView Is Nothing)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}nViewCount = nViewCount + 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}ReDim Preserve pViews(nViewCount)
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Set pViews(nViewCount) = pTempView
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Validate view
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Check if *Isometric view is found
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Dim strViewOrientation As String
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}strViewOrientation = pViews(nViewCount).GetOrientationName
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}If strViewOrientation = strIsometric Then
kadov_tag{{<spaces>}}                    kadov_tag{{</spaces>}}IsIsometricViewPresent = True
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Debug.Print pViews(nViewCount).GetOrientationName
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}Set pTempView = pTempView.GetNextView
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}Wend ' End Loop (While pTempView <> Nothing)
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}' If *Isometric view is not found, then add sheet's name to failed items list
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}If IsIsometricViewPresent = False Then
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Redimension failed item array to accommodate the new item
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}nFailedItemCount = nFailedItemCount + 1
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}ReDim Preserve FailedItemsArr(1 To 2, 1 To nFailedItemCount) As String
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Add failed entity name and its type to array
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' With these two pieces of information, the failed entity should be highlighted
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' NOTE: If you don't add entity type (e.g., "SHEET" in this case), then the entity cannot be highlighted
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Also, if you give the wrong entity type, then the entity cannot be highlighted
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}' Refer to swSelectType_e in SOLIDWORKS API Help to find the correct entity type
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}FailedItemsArr(1, nFailedItemCount) = strCurrentActiveSheet
kadov_tag{{<spaces>}}                kadov_tag{{</spaces>}}FailedItemsArr(2, nFailedItemCount) = "SHEET"
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}End If
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}
kadov_tag{{<spaces>}}            kadov_tag{{</spaces>}}pDrawingDoc.SheetNext
kadov_tag{{<spaces>}}        kadov_tag{{</spaces>}}Next nCount ' End Loop (For nCount = 1 To nSheetCount)
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}End If ' End condition (If nSheetCount > 0)
End If ' End condition (If eDocType = swDocDRAWING)

' Set Check status
If nFailedItemCount > 0 Then
kadov_tag{{<spaces>}}    kadov_tag{{</spaces>}}RunCheck = False
End If

pDrawingDoc.ActivateSheet (strOriginallyActiveSheet)

Exit Function

ON_ERROR:
Debug.Print "Check failed to execute."

End Function
```
