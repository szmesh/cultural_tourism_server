CREATE TABLE public.user (
 mid serial,
 account text DEFAULT '' NOT NULL,
 password text DEFAULT '' NOT NULL,
 gender integer DEFAULT 1,
 wechat_openid text DEFAULT '',
 wechat_unionid text DEFAULT '',
 wechat_icon text DEFAULT '',
 last_login_time timestamp(0) WITHOUT TIME ZONE,
 last_login_ip text DEFAULT '',
 status integer DEFAULT 1,
 create_time timestamp(0) WITHOUT TIME ZONE DEFAULT now() NOT NULL,
 modify_time timestamp(0) WITHOUT TIME ZONE DEFAULT now() NOT NULL,
 CONSTRAINT user_pkey PRIMARY KEY(mid)
)
WITH(oids = false);