-- Delete access to feature Edit role for all roles
delete 
from 
	t_link_feature_user_role 
where 
	idr_feature in (select 
						id_feature 
					from 
						t_feature 
					where 
						label like '%edit%' and 
						display_context like '%ROLE%')


--suppression des administrateur
delete 
from 
	t_link_role_user 
WHERE 
	idr_user_role in (select id_role from t_user_role where name_role = 'Administrator')

insert into t_link_role_user (idr_user,idr_user_role) 
select 
	t_user.user_id,
	t_user_role.id_role 
from 
	t_user,
	t_user_role 
where 
	user_logon in ('$','TO41057','TO41058','ST33058','TO76427') 
	and name_role = 'Administrator' 
	

--restore fast search for role concerned
update t_permission_access_attribute set fast_search = 1
where 
	idr_user_role in (select id_role from t_user_role where name_role like '%MAFU Change Reader%') and
	idr_infobase in (select id_infobase from infobase where object_value in ('ATACode',
'PN',
'CMS',
'FunctionnalDesignation',
'FIN',
'MODReference',
'MPReference',
'cr_RequestReference',
'MSN',
'FINCategory',
'Name',
'Reference',
'COUNTERREF'
))