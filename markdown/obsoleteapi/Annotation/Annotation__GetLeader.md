---
title: "Annotation::GetLeader"
project: ""
interface: ""
member: ""
kind: "topic"
source: "obsoleteapi/Annotation/Annotation__GetLeader.htm"
---

# Annotation::GetLeader

This method is obsolete and has been superseded
by[Annotation::GetLeaderStyle](sldworksAPI.chm::/Annotation/Annotation__GetLeaderStyle.htm).

Description

This method gets the leader display setting
for this annotation.

Syntax (OLE Automation)

retval = Annotation.GetLeader ( )

(Table)=========================================================

| Return: | (BOOL) retval | TRUE if leader display is enabled for this annotation,
FALSE if leader display is disabled for this annotation |
| --- | --- | --- |

Syntax (COM)

status = Annotation->GetLeader ( &retval )

(Table)=========================================================

| Output: | (VARIANT_BOOL) retval | TRUE if leader display is enabled for this annotation,
FALSE if leader display is disabled for this annotation |
| --- | --- | --- |
| Return: | (HRESULT) status | S_OK if successful |

Remarks

Use Annotation::SetLeader2 to enable or disable
leader display.

NOTE:Dimension
annotations do not have leaders. Therefore, this method always returns
FALSE for dimension annotations.

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
<param name="Items" value="Annotation_Object$$**$$ZGetInfoAnnotations$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Annotation\Annotation__GetLeader.htm" >
<param name="_ID" value="RelatedTopic0" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspanMetadata type="DesignerControl" startspan
<object classid="clsid:A2F1FA63-C1E6-11d2-9140-006DC83B9955"
type="application/x-oleobject"
id=RelatedTopic5>
<param name="_Version" value="65536" >
<param name="_ExtentX" value="1217" >
<param name="_ExtentY" value="556" >
<param name="_StockProps" value="13" >
<param name="ForeColor" value="0" >
<param name="BackColor" value="12632256" >
<param name="UseButton" value="0" >
<param name="ControlLabel" value="See Also" >
<param name="UseIcon" value="0" >
<param name="Items" value="EXGetDispDimGtolSFSym$$**$$" >
<param name="Image" value="" >
<param name="FontInfo" value="MS Sans Serif,8,0,," >
<param name="_CURRENTFILEPATH" value="C:\cheryle\APIHelp\sw2006\obsoleteapi\Annotation\Annotation__GetLeader.htm" >
<param name="_ID" value="RelatedTopic5" >
<param name="DialogDisplay" value="0" >
<param name="Frame" value="" >
<param name="Window" value="" >
<param name="ChmFile" value="" >
<param name="DisableJump" value="0" >
</object>Metadata type="DesignerControl" endspan
