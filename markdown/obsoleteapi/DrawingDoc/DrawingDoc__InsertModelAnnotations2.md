---
title: "DrawingDoc::InsertModelAnnotations2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/DrawingDoc/DrawingDoc__InsertModelAnnotations2.htm"
---

# DrawingDoc::InsertModelAnnotations2

This method is obsolete and has been superseded
by[DrawingDoc::InsertModelAnnotations3](sldworksAPI.chm::/DrawingDoc/DrawingDoc__InsertModelAnnotations3.htm).

Description

This method inserts model
annotations into this drawing document.

Syntax (OLE Automation)

ok = DrawingDoc.InsertModelAnnotations2 ( option,
allTypes, types, allViews, duplicateDims, hiddenFeatureDims)

(Table)=========================================================

| Input: | (long) option | 0 - All dimensions in the view 1
- All dimensions of the currently selected component (for assembly drawings) 2
- All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) allTypes | TRUE to insert all types of annotations,
FALSE uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types
as defined in swInsertAnnotation_e |
| Input: | (VARIANT_BOOL) allViews | TRUE to insert the annotations
in all views in the drawing, FALSE to insert annotations only in the selected
view |
| Input: | (VARIANT_BOOL) duplicateDims | TRUE to insert duplicate dimensions,
FALSE to eliminate duplicate dimensions |
| Input: | (VARIANT_BOOL) hiddenFeatureDims | TRUE to insert dimensions from
features that are hidden, FALSE to not insert dimensions from features
that are hidden |
| Output: | (VARIANT_BOOL) ok | TRUE if the annotations were
added, FALSE if not |

Syntax (COM)

status = DrawingDoc->InsertModelAnnotations2 (
option, allTypes, types, allViews, duplicateDims, hiddenFeatureDims, &ok)

Parameters Table Start

(Table)=========================================================

| Input: | (long) option | 0 - All dimensions in the view 1
- All dimensions of the currently selected component (for assembly drawings) 2
- All dimensions of the currently selected feature |
| --- | --- | --- |
| Input: | (VARIANT_BOOL) allTypes | TRUE to insert all types of annotations, FALSE
uses the types argument |
| Input: | (long) types | Bitwise OR of annotation types
as defined in swInsertAnnotation_e |
| Input: | (VARIANT_BOOL) allViews | TRUE to insert the annotations
in all views in the drawing, FALSE to insert annotations only in the selected
view |
| Input: | (VARIANT_BOOL) duplicateDims | TRUE to insert duplicate dimensions,
FALSE to eliminate duplicate dimensions |
| Input: | (VARIANT_BOOL) hiddenFeatureDims | TRUE to insert dimensions from features that
are hidden, FALSE to not insert dimensions from features that are hidden |
| Output: | (VARIANT_BOOL) ok | TRUE if the annotations were
added, FALSE if not |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic2
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ZReleaseNotes004$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__InsertModelAnnotations2.htm" >
<param name="_ID" value="RelatedTopic2" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="DrawingDoc_Object$$**$$ZModelAnnotations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="" >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\DrawingDoc\DrawingDoc__InsertModelAnnotations2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
