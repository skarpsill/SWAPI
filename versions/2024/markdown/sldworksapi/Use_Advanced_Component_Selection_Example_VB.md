---
title: "Use Advanced Component Selection Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Use_Advanced_Component_Selection_Example_VB.htm"
---

# Use Advanced Component Selection Example (VBA)

This example shows how to:

- load an advanced selection component query
  file.
- select, add, delete, and save a selection criteria.

'-------------------------------------------------------
' Preconditions:
'kadov_tag{{<spaces>}}1. An assembly document is active.
'kadov_tag{{<spaces>}}2. A selection criteria query file named**c:\temp\QueryMassLess.02.sqy**
'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}exists and
contains one selection criteria.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds a selection criteria to**c:\temp\QueryMassLess.02.sqy.**
' 2. Deletes first selection criteria from**c:\temp\QueryMassLess.02.sqy**.
' 3. Saves selection criteria file**c:\temp\QueryNewCriteria.sqy**.
' 4. Examine the Immediate window and**c:\temp**.
'-------------------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppSldWorks As SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swAppSldWorks = Application.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ModelDoc2 As SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
ModelDoc2 = swAppSldWorks.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
DocType As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DocType
= ModelDoc2.GetType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
DocType <> swDocASSEMBLY Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"An assembly document is not active"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Exit
Sub

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ModelDoc2.ClearSelection2True

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
AssemblyDoc As SldWorks.AssemblyDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
AssemblyDoc = ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
AdvancedSelectionCriteria As SldWorks.AdvancedSelectionCriteria

'
Get advanced component selection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
AdvancedSelectionCriteria = AssemblyDoc.GetAdvancedSelection

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Count As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Get number of advanced component selections before loading a query

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Should be 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= AdvancedSelectionCriteria.GetItemCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Before loading a query, GetItemCount returned " & Count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
CriteriaFileName As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Query file

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CriteriaFileName
= "c:\temp\QueryMassLess.02.sqy"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
LoadSuccess As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Load query file

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LoadSuccess
= AdvancedSelectionCriteria.LoadCriteria(CriteriaFileName)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Query " & CriteriaFileName & " load was"
& IIf(LoadSuccess = False, " NOT ", " ") &
"successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReportAllValues
AdvancedSelectionCriteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SelectSuccess As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select selection criteria from query list

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectSuccess
= AdvancedSelectionCriteria.Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Select was" & IIf(SelectSuccess = False, " NOT ",
" ") & "successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
AddRetVal As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Add selection criteria to query list

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AddRetVal
= AdvancedSelectionCriteria.AddItem("Document
name -- SW Special", &H4, "Gear", False)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"AddItem returned " & AddRetVal

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Print values of advanced component selection criteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReportAllValues
AdvancedSelectionCriteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Select first advanced component selection criteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SelectSuccess
= AdvancedSelectionCriteria.Select

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Select was" & IIf(SelectSuccess = False, " NOT ",
" ") & "successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
DeleteStatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Delete first component selection criteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DeleteStatus
= AdvancedSelectionCriteria.DeleteItem(0)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"DeleteItem was" & IIf(DeleteStatus = False, " NOT
", " ") & "successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReportAllValues
AdvancedSelectionCriteria

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SaveStatus As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Save query file

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}SaveStatus
= AdvancedSelectionCriteria.SaveCriteria("C:\temp\QueryNewCriteria.sqy")
'If wanted, need to specify extension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"SaveCriteria was" & IIf(SaveStatus = False, " NOT
", " ") & "successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Load query file that was just saved

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}LoadSuccess
= AdvancedSelectionCriteria.LoadCriteria("C:\temp\QueryNewCriteria.sqy")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"Query " & "c:\temp\QueryNewCriteria.sqy" &
" load was" & IIf(LoadSuccess = False, " NOT ",
" ") & "successful"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Print contents query file

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReportAllValues
AdvancedSelectionCriteria

End Sub

Function GetStringFromEnum(EnumVal As Long) As String

'From enum swAdvSelecType_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
EnumVal = &H1 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "And"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H2 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "Or"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H4000 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "is yes"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H8000 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "is no"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H8 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "is not"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H10 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "contains"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H20 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "Is_Contained_By"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H40 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "Interferes_With"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H80 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "Does_Not_Interferes_With"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H4 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "is (exactly)"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H2000 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "not ="

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H200 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "<"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H800 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "<="

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H1000 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "="

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H400 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= ">="

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ElseIf
EnumVal = &H100 Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= ">"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Else

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}GetStringFromEnum
= "Condition NOT found"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Function

Sub ReportAllValues(AdvancedSelectionCriteria As SldWorks.AdvancedSelectionCriteria)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Count As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Count
= AdvancedSelectionCriteria.GetItemCount

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"GetItemCount returned " & Count

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
i As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Property As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Condition As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Value As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
IsAnd As Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
Rindex As Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ConditionString As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
PrintString As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
IndexFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
RindexFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
AndOrFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
PropertyFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ConditionFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ValueFmt As String

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}IndexFmt
= "!@@@@@@@@"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}RindexFmt
= "!@@@@@@@@@"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}AndOrFmt
= "!@@@@@@@@@"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PropertyFmt
= "!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ConditionFmt
= "!@@@@@@@@@@@@@@@"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ValueFmt
= "#.00"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Debug.Print

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PrintString
= Format("Index", IndexFmt) & Format("Rindex",
RindexFmt) & Format("And/Or", AndOrFmt) & Format("Property",
PropertyFmt) & Format("Condition", ConditionFmt) & Format("Value",
ValueFmt)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
PrintString

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To Count - 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Rindex
= AdvancedSelectionCriteria.GetItem(i,
Property, Condition, Value, IsAnd)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ConditionString
= GetStringFromEnum(Condition)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PrintString
= Format(i, IndexFmt) & Format(Rindex, RindexFmt) & Format(IIf(IsAnd
= False, "OR", "AND"), AndOrFmt) & Format(Property,
PropertyFmt) & Format(ConditionString, ConditionFmt) & Format(Value,
ValueFmt)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
PrintString

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print

End Sub
