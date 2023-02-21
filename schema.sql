CREATE TABLE To_Do (
    task_id         SERIAL        NOT NULL,
    task_content    VARCHAR(500)  NOT NULL,
    task_status     Boolean       NOT NULL,
    PRIMARY KEY (task_id)
);