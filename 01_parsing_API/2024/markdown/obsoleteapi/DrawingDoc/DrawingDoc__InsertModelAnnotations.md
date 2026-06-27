---
title: "DrawingDoc::InsertModelAnnotations"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertModelAnnotations.htm"
---

# DrawingDoc::InsertModelAnnotations

This method is obsolete and has been superseded
by[DrawingDoc::InsertModelAnnotations2](DrawingDoc__InsertModelAnnotations2.htm).

Description

This
method inserts model annotations into this drawing document.

Syntax (OLE Automation)

retval = DrawingDoc.InsertModelAnnotations(
option, allTypes, types, allViews )

(Table)=========================================================

| Input: | (long) option | 0
- All dimensions in the view 1
- All dimensions of the currently selected component (for assembly drawings) 2
- All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (BOOL) allTypes | TRUE inserts all types of annotations, FALSE uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types as defined in swInsertAnnotation_e |
| Input: | (BOOL) allViews | TRUE inserts the annotations in all views in the drawing, FALSE inserts
annotations only in the selected view |
| Return: | (BOOL) retval | TRUE if the annotations were added, FALSE if not |

Syntax (COM)

status = DrawingDoc->InsertModelAnnotations(
option )

(Table)=========================================================

| Input: | (long) option | 0
- All dimensions in the view 1 - All dimensions
of the currently selected component (for assembly drawings) 2
- All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) allTypes | TRUE inserts all types of annotations, FALSE uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types as defined in swInsertAnnotation_e |
| Input: | (VARIANT_BOOL) allViews | TRUE inserts the annotations in all views in the drawing, FALSE inserts
annotations only in the selected view |
| Output: | (VARIANT_BOOL) retval | TRUE if the annotations were added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZModelAnnotations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__InsertModelAnnotations.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
