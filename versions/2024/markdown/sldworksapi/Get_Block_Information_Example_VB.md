---
title: "Get Block Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Block_Information_Example_VB.htm"
---

# Get Block Information Example (VBA)

This example shows how to get information about blocks in a drawing
document. This example also shows how to migrate the now obsolete and
not-supported block definition and block instance interfaces (IBlockDefinition
and IBlockInstance) to the new block definition and sketch block instance
interfaces (ISketchBlockDefinition and ISketchBlockInstance).

'----------------------------------------------
' Preconditions:
' 1. Open drawing with block definitions
' and instances.
' 2. Open the Immediate window.
'
' Postconditions: Examine the Immediate window.
'----------------------------------------------

Option Explicit

Sub main()

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swAppkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SldWorks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swModelkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.ModelDoc2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDrawkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DrawingDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBlockDefkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vBlockInstkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
OLD BLOCKS: Obsolete and not supported block

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}interfaces
as of SOLIDWORKS 2007

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Dim
swBlockDefkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.BlockDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Dim
swBlockInstkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.BlockInstance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: New block interfaces as of SOLIDWORKS 2007

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBlockDefkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchBlockDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swBlockInstkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchBlockInstance

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vNotekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swNotekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Note

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
vDispDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Variant

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDispDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.DisplayDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
swDimkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.Dimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
ikadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
jkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
kkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: Additional declaration needed for new blocks

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
SwSketchMgrkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swModel

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: For SketchBlockDefinition

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
SwSketchMgr = swModel.SketchManager

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"File = " & swModel.GetPathName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
OLD BLOCKS: Obsolete and not supported method to get block

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}definitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'vBlockDef
= swDraw.GetBlockDefinitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: New method to get block definitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBlockDef
= SwSketchMgr.GetSketchBlockDefinitions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vBlockDef) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
i = 0 To UBound(vBlockDef)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBlockDef = vBlockDef(i)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vBlockInst
= swBlockDef.GetInstances

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vNote
= swBlockDef.GetNotes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vDispDim
= swBlockDef.GetDisplayDimensions

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
OLD BLOCKS: Obsolete and not supported block-relatedkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}methods
and properties

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}"
& swBlockDef.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}UseExternalFile
= " & swBlockDef.GetUseExternalFile

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ExternalFileName
= " & swBlockDef.GetExternalFileName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: New block-related properties for external files; no

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
corresponding block definition Name property

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Block
definition linked to file? " & swBlockDef.LinkToFile

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}File
name: " & swBlockDef.FileName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vNote) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Notes:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = 0 To UBound(vNote)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swNote = vNote(j)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Tag
Namekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swNote.TagName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Textkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swNote.GetText

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vDispDim) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dimensions:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = 0 To UBound(vDispDim)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDispDim = vDispDim(j)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDim = swDispDim.GetDimension

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Namekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}FullNamekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.FullName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Typekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.GetType

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}DrivenStatekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.DrivenState

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}ReadOnlykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.ReadOnly

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Valuekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDim.GetSystemValue2("")
* 1000# & " mm"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextAllkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDispDim.GetText(swDimensionTextAll)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextPrefixkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDispDim.GetText(swDimensionTextPrefix)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextSuffixkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDispDim.GetText(swDimensionTextSuffix)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CalloutAbovekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDispDim.GetText(swDimensionTextCalloutAbove)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}CalloutBelowkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swDispDim.GetText(swDimensionTextCalloutBelow)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vBlockInst) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
j = 0 To UBound(vBlockInst)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swBlockInst = vBlockInst(j)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}vNote
= swBlockInst.GetAttributes

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
NEW BLOCKS: Get block instance Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Name
of block instance: " & swBlockInst.Name

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}''''''''''''''''''''''''''''''''''''''''''''''''''''''

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Block
instance(" & j & "):"

' 1 radian = 180º/ p = 57.295779513º or approximately 57.3º

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Anglekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swBlockInst.Angle* 57.3 & " deg"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Scalekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swBlockInst.Scale

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}TextDisplaykadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swBlockInst.TextDisplay

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}If
Not IsEmpty(vNote) Then

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Notes:"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}For
k = 0 To UBound(vNote)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swNote = vNote(k)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Tag
Namekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swNote.TagName

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Textkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}=
" & swNote.GetText

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
""

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
k

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
j

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
"kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}------------------------------------"

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Next
i

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}End
If

End Sub

'------------------------------------
