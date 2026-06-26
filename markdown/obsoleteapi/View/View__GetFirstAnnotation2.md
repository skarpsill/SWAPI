---
title: "View::GetFirstAnnotation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/View/View__GetFirstAnnotation2.htm"
---

# View::GetFirstAnnotation2

This method is obsolete and has been superseded
by[View::GetFirstAnnotation3](sldworksAPI.chm::/View/View__GetFirstAnnotation3.htm).

Description

This method gets the first annotation in the view.

Syntax (OLE Automation)

retval = View.GetFirstAnnotation2( )

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in the view |
| --- | --- | --- |

Syntax (COM)

status = View->IGetFirstAnnotation2(
&retval )

(Table)=========================================================

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the view |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful. |

Remarks

The difference between this method and the now obsolete View::GetFirstAnnotation
is that this method retrieves any display dimension, including suppressed,
hidden, or dangling dimensions. The sheet must be visible. See Sheet::SheetFormatVisible.

A dimension becomes suppressed or hidden when you specifically select
a dimension and hide it or when you select a feature and say hide all
dimensions. If you need to filter out these dimensions, you must use Annotation::Visibleto check that status.

If the annotation is on a layer that is not shown, the annotation is
still returned.

If annotations are not displayed or any specific types of annotations
are not displayed due to the end-user setting some annotation properties,
use ModelDoc2::GetUserPreferenceToggle to discover those situations.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="View_Object$$**$$View$$**$$ZModelAnnotations$$**$$SheetFormatVisible$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetFirstAnnotation2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="Get_Entities_Attached_To_Cosmetic_Thread_Example$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2005\obsoleteapi\View\View__GetFirstAnnotation2.htm" >
<param name="_ID" value="RelatedTopic1" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
