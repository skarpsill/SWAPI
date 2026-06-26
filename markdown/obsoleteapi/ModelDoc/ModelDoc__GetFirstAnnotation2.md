---
title: "ModelDoc::GetFirstAnnotation2"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstAnnotation2.htm"
---

# ModelDoc::GetFirstAnnotation2

This
method is obsolete and has been superseded by[ModelDoc2::GetFirstAnnotation2](sldworksAPI.chm::/ModelDoc2/ModelDoc2__GetFirstAnnotation2.htm).

Description

This method gets the first annotation in the
model.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstAnnotation2(
)

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in
the model |
| --- | --- | --- |

Syntax (COM)

status
= ModelDoc->IGetFirstAnnotation2( &retval )

(Table)=========================================================

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the model |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For part and assembly documents, this method returns the first Annotation
object in the model. For drawing documents, access annotations using View::GetFirstAnnotation2.

The difference between ModelDoc::GetFirstAnnotation and ModelDoc::GetFirstAnnotation2is that ModelDoc::GetFirstAnnotation2retrieves any display dimension, including
suppressed, hidden, or dangling dimensions.

A dimension becomes suppressed or hidden when you specifically select
a dimension and hide it, or when you select a feature and say hide all
dimensions. So if you need to filter out these dimensions, you will have
to use the Annotation::VisibleAPI
to check that status.

If the annotation is on a layer that isn't shown, the annotation will
still be returned.

If annotations are not displayed, or any specific types of annotations
are not displayed due to user Annotation Properties settings, the[ModelDoc::GetUserPreferenceToggle](ModelDoc__GetUserPreferenceToggle.htm)API can be used to discover those situations.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
style="width: 1px; height: 1px;"
width=1
height=1>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="26" >
<param name="_ExtentY" value="26" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="13160660" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="ModelDoc_Object$$**$$ZModelAnnotations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2004\obsoleteapi\ModelDoc\ModelDoc__GetFirstAnnotation2.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
