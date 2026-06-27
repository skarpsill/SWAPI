---
title: "ModelDoc::GetFirstAnnotation"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__GetFirstAnnotation.htm"
---

# ModelDoc::GetFirstAnnotation

This
method is obsolete and has been superseded by[ModelDoc::GetFirstAnnotation2](ModelDoc__GetFirstAnnotation2.htm).

Description

This method gets the first
annotation in the model.

Syntax (OLE Automation)

retval = ModelDoc.GetFirstAnnotation(
)

(Table)=========================================================

| Return: | (LPDISPATCH) retval | Dispatch object for the first Annotation object in
the model |
| --- | --- | --- |

Syntax (COM)

status = ModelDoc->IGetFirstAnnotation(
&retval )

(Table)=========================================================

| Output: | (LPANNOTATION) retval | Pointer to the first Annotation object in the model |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

For part and assembly documents, this method returns the first Annotation
object in the model. For drawing documents, access the annotations using
View::GetFirstAnnotation.

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
<param name="_CURRENTFILEPATH" value="C:\Home\Oneill\sw2003\ModelDoc\ModelDoc__GetFirstAnnotation.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
