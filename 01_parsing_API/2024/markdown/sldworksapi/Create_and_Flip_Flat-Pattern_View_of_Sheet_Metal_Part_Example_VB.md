---
title: "Create and Flip Flat-Pattern View of Sheet Metal Part Example (VB)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Flip_Flat-Pattern_View_of_Sheet_Metal_Part_Example_VB.htm"
---

# Create and Flip Flat-Pattern View of Sheet Metal Part Example (VB)

This example shows how to create and flip a flat-pattern view of a sheet
metal part.

'------------------------------------------

'

' Problem:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}The
drawing view must be of the part in a flattened

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}state
and without bend lines. This is necessary so the

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}file
is suitable for export to DXF for subsequent import

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}into
laser cutting software, which normally only requires

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}the
outline of the profile to be cut.

'

' Preconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}1)
Sheet metal part is open.

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}2)
Adjust paper template size, height, and width.

'

' Postconditions:

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Anew
A1 sized drawing is generated with

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}a
flattened view of the sheet metal part

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}with
no bend lines showing.

'

'-------------------------------------------

Option Explicit

Public Enum swDwgPaperSizes_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperAsize
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperAsizeVertical
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperBsize
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperCsize
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperDsize
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperEsize
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA4size
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA4sizeVertical
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA3size
= 8

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA2size
= 9

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA1size
= 10

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPaperA0size
= 11

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgPapersUserDefined
= 12

End Enum

Public Enum swDwgTemplates_e

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateAsize
= 0

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateAsizeVertical
= 1

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateBsize
= 2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateCsize
= 3

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateDsize
= 4

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateEsize
= 5

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA4size
= 6

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA4sizeVertical
= 7

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA3size
= 8

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA2size
= 9

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA1size
= 10

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateA0size
= 11

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateCustom
= 12

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swDwgTemplateNone
= 13

End Enum

' Paper size in millimeters

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Akadov_tag{{<spaces>}}kadov_tag{{</spaces>}}216
x 279

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Bkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}279
x 432

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ckadov_tag{{<spaces>}}kadov_tag{{</spaces>}}432
x 559

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}559
x 864

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Ekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}864
x 1118

'

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A0kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}841
x 1189

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A1kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}594
x 841

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A2kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}420
x 594

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A3kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}297
x 420

'kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}A4kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}210
x 297

Const TemplateSizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long = swDwgTemplateA1size

Const PaperSizekadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Long = swDwgPaperA1size

Const PaperWidthkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 0.841kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Meters

Const PaperHeightkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Double = 0.594kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}'
Meters

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
swViewkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
SldWorks.View

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Dim
bRetkadov_tag{{<spaces>}}kadov_tag{{</spaces>}}As
Boolean

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swApp = CreateObject("SldWorks.Application")

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swModel = swApp.ActiveDoc

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swDraw = swApp.NewDrawing2(TemplateSize,
"", PaperSize, _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PaperWidth,
PaperHeight)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Set
swView = swDraw.CreateFlatPatternViewFromModelView3(
_

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swModel.GetPathName, "", _

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}PaperWidth
/ 2, PaperHeight / 2, 0#, True, True)

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
swView.GetName2

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
swView.FlipView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}swView.FlipView= False

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}Debug.Print
swView.FlipView

kadov_tag{{<spaces>}}kadov_tag{{</spaces>}}

End Sub
