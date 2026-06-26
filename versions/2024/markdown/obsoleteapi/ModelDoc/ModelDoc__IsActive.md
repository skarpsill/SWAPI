---
title: "ModelDoc::IsActive"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/ModelDoc/ModelDoc__IsActive.htm"
---

# ModelDoc::IsActive

This method is obsolete
and has been superseded by[ModelDoc2::IsActive](sldworksAPI.chm::/ModelDoc2/ModelDoc2__IsActive.htm).

Description

This method determines if the specified assembly component is displayed;
this is, the show and hide functionality associated with assembly components.

Syntax (OLE Automation)

retval = ModelDoc.IsActive ( compStr)

(Table)=========================================================

| Input: | (BSTR) compStr | Name specification of the component |
| --- | --- | --- |
| Return: | (BOOL) retval | TRUE if model is shown, FALSE if model is hidden |

Syntax (COM)

status = ModelDoc->IsActive ( compStr,
&retval )

(Table)=========================================================

| Input: | (BSTR) compStr | Name specification of the component |
| --- | --- | --- |
| Output: | (VARIANT_BOOL) retval | TRUE if model is shown, FALSE if model is hidden |
| Return: | (HRESULT)status | S_OK if successful |

Remarks

The compStrparameter is the
full assembly component name designation. The format of the name designation
is:

parentModel/childModel

where the child model is the model you wish to determine the display
status. For example, if you want to determine the display status of a
part named SPOKE.SLDPRT and if this part was a child of WHEEL.SLDPRT,
which itself is a child of AXIS.SLDPRT, then you would specify compStr
as follows:

AXIS/WHEEL/SPOKE

TIP:The assembly component
name designation is shown in the lower-eft hand corner of the SolidWorks
application when an assembly component is selected.

Metadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic0
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
<param name="Items" value="ModelDoc_Object$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="D:\APIHelp\sw2003\ModelDoc\ModelDoc__IsActive.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
